from enums import InstrumentType, TradingStatus
from pydantic import BaseModel


class Instrument(BaseModel):
    """
    Схема данных инструмента
    """

    # Figi-идентификатор инструмента.
    figi: str
    # Тикер инструмента.
    ticker: str
    # Класс-код инструмента.
    class_code: str
    # Isin-идентификатор инструмента.
    isin: str
    # Лотность инструмента. Возможно совершение операций только на количества
    # ценной бумаги, кратные параметру lot.
    lot: int
    # Валюта расчётов.
    currency: str
    # Коэффициент ставки риска длинной позиции по инструменту.
    klong: float
    # Коэффициент ставки риска короткой позиции по инструменту.
    kshort: float
    # Ставка риска минимальной маржи в лонг. Подробнее: ставка риска в лонг
    dlong: float
    # Ставка риска минимальной маржи в шорт. Подробнее: ставка риска в шорт
    dshort: float
    # Ставка риска начальной маржи в лонг. Подробнее: ставка риска в лонг
    dlong_min: float
    # Ставка риска начальной маржи в шорт. Подробнее: ставка риска в шорт
    dshort_min: float
    # Признак доступности для операций в шорт.
    short_enabled_flag: bool
    # Название инструмента.
    name: str
    # Торговая площадка.
    exchange: str
    # Код страны риска, т.е. страны, в которой компания ведёт
    # основной бизнес.
    country_of_risk: str
    # Наименование страны риска, т.е. страны, в которой
    # компания ведёт основной бизнес.
    country_of_risk_name: str
    # Тип инструмента.
    instrument_type: InstrumentType
    # Текущий режим торгов инструмента
    trading_status: TradingStatus
    # Признак внебиржевой ценной бумаги.
    otc_flag: bool
    # Признак доступности для покупки.
    buy_available_flag: bool
    # Признак доступности для продажи.
    sell_available_flag: bool
    # Шаг цены.
    min_price_increment: float
    # Признак доступности торгов через API.
    api_trade_available_flag: bool
