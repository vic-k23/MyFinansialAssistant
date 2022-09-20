from decimal import Decimal
from os import getenv
from re import match
from xml.etree.ElementTree import fromstring

import aiohttp
import aioredis
from dotenv import load_dotenv

from exception_logger import log_exception


class CBRExchangeRate:
    """
    Класс для подключения к сайту ЦБР для получения курса валют
    """

    def __init__(self):
        """
        Инициализация экземпляра класса.
        Значения по-умолчанию:
            base_url = "http://www.cbr.ru"
            exchange_script = "/scripts/XML_daily.asp"
            currencies_descriptions = "/scripts/XML_valFull.asp"
            redis_host = getenv('REDIS_HOST', default='localhost')
            redis_port = getenv('REDIS_PORT', default='6379')
            redis_user = getenv('REDIS_USER', default='user')
            redis_password = getenv('REDIS_PASSWORD')
            redis_url = f"redis://{redis_host}:{redis_port}"
        """

        self.__base_url = "http://www.cbr.ru"
        self.__exchange_script = "/scripts/XML_daily.asp"
        self.__currencies_descriptions = "/scripts/XML_valFull.asp"

        try:

            load_dotenv(override=True)
            redis_host = getenv('REDIS_HOST', default='localhost')
            redis_port = getenv('REDIS_PORT', default='6379')
            redis_user = getenv('REDIS_USER', default='user')
            redis_password = getenv('REDIS_PASSWORD')
            self.__redis_url = f"redis://{redis_host}:{redis_port}"

            self.__session = aiohttp.ClientSession(self.__base_url)
            self.__redis = aioredis.from_url("redis://localhost",
                                             username=redis_user,
                                             password=redis_password,
                                             decode_responses=True)

        except Exception as ex:
            log_exception("Ошибка инициализации основного объекта:", ex)

    async def __aenter__(self):
        """
        Методы поддержки контекстного менеджера
        """

        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """
        Методы поддержки контекстного менеджера
        """

        await self.__session.close()
        return True

    async def __redis_connected(self) -> bool:
        """
        Проверка подключения к Redis
        :return: True если подключение к серверу доступно.
        :rtype: bool
        """

        try:
            result = await self.__redis.ping()
            if result:
                return True
            return False
        except aioredis.exceptions.ConnectionError as conn_err:
            log_exception("Connection error.", conn_err)
            return False
        except Exception as ex:
            print(type(ex))
            log_exception("Нет подключения к Redis.\n", ex)
            return False

    async def __fetch_currencies(self, **kwargs) -> str:
        """
        Отправляет запрос на сайт ЦБ на получение списка доступных валют
        :return: текст ответа сайта ЦБ
        :rtype: str
        """

        async with self.__session.get(self.__currencies_descriptions) as cbr_response:
            assert cbr_response.status == 200
            return await cbr_response.text()

    async def __fetch_exchange_rates(self, **kwargs) -> str:
        """
        Отправляет запрос на сайт ЦБ на получение списка доступных валют
        :return: текст ответа сайта ЦБ
        :rtype: str
        """

        async with self.__session.get(self.__exchange_script) as cbr_response:
            assert cbr_response.status == 200
            return await cbr_response.text()

    async def __store_exchange_rate(self, currency: str, key_date: str, value_rate: str) -> int:
        """
        Stores given exchange rates of given currency to redis
        :param currency: the name of currency (from the list, returned by get_currencies)
        :type currency: str
        :param key_date: the exchange rate date of currency in format 'dd/mm/yyyy'
        :type key_date: str
        :param value_rate: the exchange rate value of currency for nominal in format nominal=value
        :type value_rate: str
        :return: the number of fields that were added
        :rtype: int
        """

        try:
            if match(r'\d\d/\d\d/\d\d\d\d', key_date):
                return await self.__redis.hset(name=currency, key=key_date, value=value_rate)
            else:
                log_exception("Неверный формат даты! Должен быть dd/mm/yyyy")

        except Exception as ex:
            log_exception("Не удалось сохранить курс:\n", ex)

    async def __get_exchange_rate(self, currency: str, key_date: str) -> str | None:
        """
        Request exchange rates from redis
        :param currency: the currency which rate you need
        :type currency: str
        :param key_date: the key, which is a date for exchange rate in format "dd/mm/yyyy"
        :type key_date: str
        :return: the exchange rate of currency for given date in format nominal=cost
        :rtype: str
        """

        if currency.upper() == "RUB":
            return "1=1.0"
        try:
            if await self.__redis_connected() and await self.__redis.hexists(name=currency, key=key_date):
                return await self.__redis.hget(name=currency, key=key_date)
            else:
                return None

        except Exception as ex:
            log_exception(f"Не удалось получить курс валюты на дату {key_date}:\n", ex)

    async def close(self):
        """
        Явное закрытие соединений
        :return:
        :rtype:
        """
        try:
            await self.__redis.close()
            await self.__session.close()
        except Exception as ex:
            log_exception("Ошибка при закрытии соединений в клиенте ЦБР", ex)

    async def get_currencies(self) -> list:
        """
        Создаёт список словарей с описанием валют
        :return: список словарей, описывающих валюту
        :rtype:
        """

        currencies = []
        currencies_xml = fromstring(await self.__fetch_currencies())

        if currencies_xml:
            for currency in currencies_xml:
                currencies.append({
                    "name": currency.find('Name').text,
                    "eng_name": currency.find('EngName').text,
                    "nominal": int(currency.find('Nominal').text),
                    "code": currency.find('ISO_Char_Code').text
                    })

        return currencies

    async def get_currency_names(self) -> list:
        """
        Создаёт список названий валют согласно ISO стандарту
        :return: список названий валют
        """
        currencies = []
        currencies_xml = fromstring(await self.__fetch_currencies())
        if currencies_xml:
            for currency in currencies_xml:
                currencies.append(currency.find('ISO_Char_Code').text)

        return currencies

    async def get_exchange_currency(self, currency_code: str, exchange_date: str) -> dict:
        """
        Создаёт словарь вида {name, nominal, cost}, отражающий курс валюты на указанную дату
        :param currency_code: трёхсимвольный код из словаря, возвращаемого в списке функцией get_currencies
        :param exchange_date: дата, на которую нужно узнать курс валюты по отношению к рублю в формате dd/mm/yyyy
        :return: dict{name, nominal, cost}
        """

        exchange_currency = {}

        try:
            if match(r'\d\d/\d\d/\d\d\d\d', exchange_date):

                exchange_rate = await self.__get_exchange_rate(currency_code, exchange_date)
                if exchange_rate is not None:
                    nominal, cost = exchange_rate.split('=', 1)
                    exchange_currency['code'] = currency_code.upper()
                    exchange_currency['nominal'] = int(nominal)
                    exchange_currency['cost_decimal'] = Decimal(cost.replace(',', '.'))
                    exchange_currency['cost_str'] = f"\u20BD {cost}"

                else:
                    exchange_currencies_xml = fromstring(await self.__fetch_exchange_rates(date_req=exchange_date))
                    for currency in exchange_currencies_xml:
                        if currency.find('CharCode').text == currency_code.upper():
                            exchange_currency['code'] = currency.find('CharCode').text
                            exchange_currency['nominal'] = int(currency.find('Nominal').text)
                            exchange_currency['cost_decimal'] = Decimal(currency.find('Value').text.replace(',', '.'))
                            exchange_currency['cost_str'] = f"\u20BD {currency.find('Value').text}"

                            # Save the exchange rate to redis
                            if await self.__redis_connected():
                                await self.__store_exchange_rate(
                                        currency_code.upper(),
                                        exchange_date,
                                        f"{exchange_currency['nominal']}={currency.find('Value').text}")
                            break

            else:
                log_exception("Неверный формат даты! Должен быть dd/mm/yyyy")

            return exchange_currency

        except Exception as ex:
            log_exception(f"Не удалось получить курс валюты {currency_code}:", ex)


if __name__ == '__main__':
    from pprint import pprint
    from asyncio import run


    async def try_lib():
        try:
            async with CBRExchangeRate() as cbr:
                pprint(await cbr.get_currencies())
                print(20 * '=')
                print()
                pprint(await cbr.get_exchange_currency('USD', '19/11/2021'))
        except Exception as ex:
            log_exception("", ex)


    run(try_lib())
