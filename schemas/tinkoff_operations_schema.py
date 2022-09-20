from pydantic import BaseModel
from decimal import Decimal

from enums import InstrumentType


class PortfolioPosition(BaseModel):
    """
    Позиция портфеля (инструмент в портфеле)
    """

    # Figi - идентификатора инструмента.
    figi: str
    # Тип инструмента.
    instrument_type: InstrumentType
    # Количество инструмента в портфеле в штуках.
    quantity: int
    # Средневзвешенная цена позиции. Возможна задержка до секунды для пересчёта.
    average_position_price: Decimal
    # Текущая рассчитанная доходность позиции.
    expected_yield: Decimal
    # Текущий НКД.
    current_nkd: Decimal
    # Средняя цена позиции в пунктах(для фьючерсов). Возможна задержка до секунды для пересчёта.
    average_position_price_pt: Decimal
    # Текущая цена за 1 инструмент. Для получения стоимости лота требуется умножить на лотность инструмента.
    current_price: Decimal
    # Средняя цена позиции по методу FIFO. Возможна задержка до секунды для пересчёта.
    average_position_price_fifo: Decimal
    # Количество лотов в портфеле.
    quantity_lots: int
    # Заблокировано.
    blocked: bool
