import datetime as DT
import decimal
from decimal import Decimal
from math import fabs
from os import getenv

from dotenv import load_dotenv
from grpc import ssl_channel_credentials
from grpc.aio import secure_channel

import grpc_pb2.common_pb2 as _common_pb
import grpc_pb2.instruments_pb2 as _instruments_pb
import grpc_pb2.instruments_pb2_grpc as _instruments_grpc
import grpc_pb2.operations_pb2 as _operations_pb
import grpc_pb2.operations_pb2_grpc as _operations_grpc
import grpc_pb2.users_pb2 as _users_pb
import grpc_pb2.users_pb2_grpc as _users_grpc
from cbr_lib import CBRExchangeRate
from enums import AccountType, AccountStatus, OperationType, OperationStatus, InstrumentType, TradingStatus
from exception_logger import log_exception


# Loading auth-token
load_dotenv()
TINKOFF_TOKEN = getenv('TINKOFF_TOKEN')


class TinkoffClient:
    """
    A class for working with Tinkoff investing portal
    """

    def __init__(self, t: str = TINKOFF_TOKEN):
        """
        Returns a gRPC secure channel to tinkoff invest
        :param t: authentication token
        """

        self.TINKOFF_URI = "invest-public-api.tinkoff.ru:443"

        if t is not None:
            self.token = t

        # необходимо с каждым запросом передавать токен, что в grpc выполняется через метаданные
        self.metadata = (('authorization', f"bearer {self.token}"),)
        my_ssl_credentials = ssl_channel_credentials()
        self.channel = secure_channel(self.TINKOFF_URI, credentials=my_ssl_credentials)
        self.__cbr_client = CBRExchangeRate()

    def __str__(self) -> str:
        """
        Возвращает строковое представление экземпляра класса TinkoffClient
        :return: строковое представление канала
        """
        return str(self.channel)

    async def __aenter__(self):
        """Context manager support"""
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> bool:
        """Context manager support"""
        await self.channel.__aexit__(exc_type, exc_val, exc_tb)
        await self.__cbr_client.__aexit__(exc_type, exc_val, exc_tb)
        return True

    def _convert_money_value(self, money: _common_pb.MoneyValue) -> Decimal:
        """
        Конвертирует MoneyValue в Decimal
        :param money: экземпляр MoneyValue
        :return: экземпляр Decimal
        """
        value = None

        try:
            if isinstance(money, _common_pb.MoneyValue):
                value = Decimal(f"{money.units if money.units is not None else 0}"
                                f".{int(fabs(money.nano if money.nano is not None else 0))}")
            else:
                value = Decimal()
        except decimal.ConversionSyntax as ex:
            # log_exception("Error while converting money value", ex)
            print(ex)
        finally:
            return value

    async def _get_payment_in_rub(self, value: Decimal, cur: str, dt: DT.datetime) -> Decimal:
        """
        Конвертирует величину в указанной валюте в величину в рублях РФ на указанную дату
        :param value: величина в указанной валюте
        :type value: Decimal
        :param cur: валюта указанной величины
        :type cur: str
        :param dt: дата, на которую нужно использовать курс валюты для конвертации в рубли РФ
        :type dt: datetime.datetime
        :return: величина в рублях РФ по курсу ЦБ РФ указанной валюты на указанную дату
        :rtype: Decimal
        """

        exchange_currency = await self.__cbr_client.get_exchange_currency(cur, dt.strftime('%d/%m/%Y'))
        exchage_course = exchange_currency.get("cost_decimal") if "cost_decimal" in exchange_currency else 0

        return self._convert_money_value(value) * exchage_course

    async def close(self):
        try:
            await self.__cbr_client.close()
            await self.channel.close(grace=1000.0)
        except Exception as ex:
            log_exception("Ошибка при закрытии соединений в клиенте Тинькофф", ex)

    async def get_accounts(self) -> list:
        """
        Создаёт список брокерских счетов пользователя
        :return: список счетов пользователя
        """

        accounts_list = []
        try:
            stub = _users_grpc.UsersServiceStub(self.channel)
            response = await stub.GetAccounts(_users_pb.GetAccountsRequest(), metadata=self.metadata)

            if response:
                for account in response.accounts:
                    accounts_list.append({
                        "id": account.id,
                        "type": AccountType(account.type),
                        "name": str(account.name),
                        "status": AccountStatus(account.status),
                        "opened": DT.datetime.fromtimestamp(account.opened_date.seconds
                                                            + account.opened_date.nanos * 1e-9),
                        "closed": DT.datetime.fromtimestamp(account.closed_date.seconds
                                                            + account.closed_date.nanos * 1e-9)
                        })
        except Exception as ex:
            log_exception("Error while getting accounts list", ex)
        finally:
            return accounts_list

    async def get_portfolio(self, account_id: str) -> list:
        """
        Список инструментов в портфеле
        :return:
        :rtype:
        """

        portfolio_positions = []

        try:
            stub = _operations_grpc.OperationsServiceStub(self.channel)
            request = _operations_pb.OperationsRequest()
            setattr(request, 'account_id', account_id)
            response = await stub.GetPortfolio(request, metadata=self.metadata)

            for position in response.positions:
                portfolio_positions.append(
                        {
                            'figi': position.figi,
                            'instrument_type': InstrumentType[str(position.instrument_type).upper()],
                            'quantity': position.quantity.units,
                            'average_position_price': self._convert_money_value(position.average_position_price),
                            'expected_yield': self._convert_money_value(position.expected_yield),
                            'current_nkd': self._convert_money_value(position.current_nkd),
                            'current_price': self._convert_money_value(position.current_price),
                            'average_position_price_fifo': self._convert_money_value(
                                    position.average_position_price_fifo),
                            'quantity_lots': position.quantity_lots.units,
                            }
                        )

            return portfolio_positions
        except Exception as ex:
            log_exception("Error while getting portfolio: ", ex)

    async def get_instrument_info(self, figi: str) -> dict:
        """
        Получает информацию по инструменту
        :param figi: Идентификатор FIGI инструмента
        :return: словарь параметров инструмента
        """
        if figi is None or figi == '':
            return {}
        instrument_info = {}
        try:
            stub = _instruments_grpc.InstrumentsServiceStub(self.channel)
            request = _instruments_pb.InstrumentRequest()
            setattr(request, 'id_type', _instruments_pb.INSTRUMENT_ID_TYPE_FIGI)
            setattr(request, 'id', figi)
            response = await stub.GetInstrumentBy(request, metadata=self.metadata)
            """
            Instrument:
            figi string	Figi-идентификатор инструмента.
            ticker string	Тикер инструмента.
            class_code - string - Класс-код инструмента.
            isin - string - Isin-идентификатор инструмента.
            lot - int32 - Лотность инструмента. Возможно совершение операций только на количества ценной бумаги, кратные 
                            параметру lot.
            currency - string - Валюта расчётов.
            klong - Quotation - Коэффициент ставки риска длинной позиции по инструменту.
            kshort - Quotation - Коэффициент ставки риска короткой позиции по инструменту.
            dlong - Quotation - Ставка риска минимальной маржи в лонг. Подробнее: ставка риска в лонг
            dshort - Quotation - Ставка риска минимальной маржи в шорт. Подробнее: ставка риска в шорт
            dlong_min - Quotation - Ставка риска начальной маржи в лонг. Подробнее: ставка риска в лонг
            dshort_min - Quotation - Ставка риска начальной маржи в шорт. Подробнее: ставка риска в шорт
            short_enabled_flag - bool - Признак доступности для операций в шорт.
            name - string - Название инструмента.
            exchange - string - Торговая площадка.
            country_of_risk - string - Код страны риска, т.е. страны, в которой компания ведёт основной бизнес.
            country_of_risk_name - string - Наименование страны риска, т.е. страны, в которой компания ведёт основной 
                                            бизнес.
            instrument_type - string - Тип инструмента.
            trading_status - SecurityTradingStatus - Текущий режим торгов инструмента.
            otc_flag - bool - Признак внебиржевой ценной бумаги.
            buy_available_flag - bool - Признак доступности для покупки.
            sell_available_flag - bool - Признак доступности для продажи.
            min_price_increment - Quotation - Шаг цены.
            api_trade_available_flag - bool - Признак доступности торгов через API.
            """
            instrument_info = {
                "figi": response.instrument.figi,  # Figi-идентификатор инструмента.
                "ticker": response.instrument.ticker,  # Тикер инструмента.
                "class_code": response.instrument.class_code,  # Класс-код инструмента.
                "isin": response.instrument.isin,  # Isin-идентификатор инструмента.
                "lot": int(response.instrument.lot),
                # Лотность инструмента. Возможно совершение операций только на количества
                # ценной бумаги, кратные параметру lot.
                "currency": response.instrument.currency,  # Валюта расчётов.
                # Коэффициент ставки риска длинной позиции по инструменту.
                "klong": self._convert_money_value(response.instrument.klong),
                # Коэффициент ставки риска короткой позиции по инструменту.
                "kshort": self._convert_money_value(response.instrument.kshort),
                "dlong": self._convert_money_value(response.instrument.dlong),
                # Ставка риска минимальной маржи в лонг. Подробнее: ставка риска в лонг
                "dshort": self._convert_money_value(response.instrument.dshort),
                # Ставка риска минимальной маржи в шорт. Подробнее: ставка риска в шорт
                "dlong_min": self._convert_money_value(response.instrument.dlong_min),
                # Ставка риска начальной маржи в лонг. Подробнее: ставка риска в лонг
                "dshort_min": self._convert_money_value(response.instrument.dshort_min),
                # Ставка риска начальной маржи в шорт. Подробнее: ставка риска в шорт
                "short_enabled_flag": response.instrument.short_enabled_flag,
                # Признак доступности для операций в шорт.
                "name": response.instrument.name,  # Название инструмента.
                "exchange": response.instrument.exchange,  # Торговая площадка.
                "country_of_risk": response.instrument.country_of_risk,
                # Код страны риска, т.е. страны, в которой компания ведёт
                # основной бизнес.
                "country_of_risk_name": response.instrument.country_of_risk_name,
                # Наименование страны риска, т.е. страны, в которой
                # компания ведёт основной бизнес.
                "instrument_type": InstrumentType[str(response.instrument.instrument_type).upper()],  # Тип инструмента.
                "trading_status": TradingStatus(response.instrument.trading_status),  # Текущий режим торгов инструмента
                "otc_flag": response.instrument.otc_flag,  # Признак внебиржевой ценной бумаги.
                "buy_available_flag": response.instrument.buy_available_flag,  # Признак доступности для покупки.
                "sell_available_flag": response.instrument.sell_available_flag,  # Признак доступности для продажи.
                "min_price_increment": self._convert_money_value(response.instrument.min_price_increment),  # Шаг цены.
                # Признак доступности торгов через API.
                "api_trade_available_flag": response.instrument.api_trade_available_flag,
                }
        except Exception as ex:
            log_exception("Error while getting instrument info:", ex)
        finally:
            return instrument_info

    async def get_operations(self, account_id: str, from_date: DT.datetime, to_date: DT.datetime,
                             state: _operations_pb.OperationState = _operations_pb.OPERATION_STATE_UNSPECIFIED,
                             type_=None, currencies=None, figi="") -> list:
        """
        Создаёт описание портфеля по указанному счёту
        :param figi: FIGI бумаги, по которой интересует операция
        :param currencies: список валют, в которых совершались операции
        :param type_: тип операции
        :param state: статус операции для фильтрации
        :param to_date: дата, до которой нужно получить список операций
        :param from_date: дата, с которой нужно получить список операций
        :param account_id: идентификатор счёта полученный с помощью функции get_accounts
        :return: список операций по счёту
        """
        if currencies is None:
            currencies = []
        # if type_ is None:
        #     type_ = [_operations_pb.OPERATION_TYPE_UNSPECIFIED,
        #              _operations_pb.OPERATION_TYPE_BUY,
        #              _operations_pb.OPERATION_TYPE_BUY]
        operations_list = []
        # try:
        stub = _operations_grpc.OperationsServiceStub(self.channel)
        request = _operations_pb.OperationsRequest()
        setattr(request, 'account_id', account_id)
        request_from = getattr(request, 'from')
        request_from.seconds = int(from_date.timestamp())
        request_from.nanos = 0
        request_to = getattr(request, 'to')
        request_to.seconds = int(to_date.timestamp())
        request_to.nanos = 0
        setattr(request, 'state', state)
        setattr(request, 'figi', figi)
        response = await stub.GetOperations(request, metadata=self.metadata)
        for operation in response.operations:
            if (type_ is None or operation.operation_type in type_) \
                    and (len(currencies) == 0 or operation.currency in currencies):
                # instrument = None
                # if operation.figi != '' and operation.figi is not None:
                #     instrument = await self.get_instrument_info(operation.figi)

                operation_date = DT.datetime.fromtimestamp(operation.date.seconds + operation.date.nanos * 1e-9)
                payment_in_rub = await self._get_payment_in_rub(operation.payment,
                                                                operation.currency,
                                                                operation_date)
                operations_list.append({
                    "id": operation.id,
                    "parent_operation_id": operation.parent_operation_id,
                    "currency": operation.currency,
                    "payment": self._convert_money_value(operation.payment),
                    "payment_rub": payment_in_rub,
                    "price": self._convert_money_value(operation.price),
                    "state": OperationStatus(operation.state),
                    "quantity": operation.quantity,
                    "quantity_rest": operation.quantity_rest,
                    "figi": operation.figi,
                    # Тип инструмента. Возможные значения:
                    #     bond — облигация;
                    #     share — акция;
                    #     currency — валюта;
                    #     etf — фонд;
                    #     futures — фьючерс.
                    "instrument_type":
                        (InstrumentType[str(operation.instrument_type).upper()] if operation.instrument_type
                         else operation.instrument_type),
                    # "instrument_isin": instrument.get("isin") if instrument else '',
                    # "instrument_lot": instrument.get("lot") if instrument else 1,
                    # "instrument_name": instrument.get("name") if instrument else '',
                    # "instrument_exchange": instrument.get("exchange") if instrument else '',
                    # "instrument_country_of_risk": instrument.get("country_of_risk") if instrument else '',
                    "date": operation_date,
                    "type": operation.type,
                    "operation_type": OperationType(operation.operation_type)
                    })
        # except Exception as ex:
        #     log_exception("Error while getting operations list:", ex)

        return operations_list


if __name__ == '__main__':
    from pprint import pprint
    from datetime import datetime
    import asyncio


    async def get_all_accounts():
        async with TinkoffClient() as c:
            # accounts = await c.get_accounts()
            # if len(accounts) > 0:
            #     print(f"{'Название':20}\t"
            #           f"{'Тип':11}\t"
            #           f"{'Статус':11}\t"
            #           f"Дата открытия")
            #     print("=" * 57)
            #     for acc in accounts:
            #         print(f"{acc.get('name'):20}\t"
            #               f"{acc.get('type').name:11}\t"
            #               f"{acc.get('status').name:11}\t"
            #               f"{acc.get('opened'): %d.%m.%Y}"
            #               )
            portfolio = await c.get_operations("2099628725",
                                               datetime(datetime.now().year, 1, 1, 0, 0, 0, 0),
                                               datetime.now())
            # figi="BBG000KHWT55")
            pprint(portfolio)


    asyncio.run(get_all_accounts())
