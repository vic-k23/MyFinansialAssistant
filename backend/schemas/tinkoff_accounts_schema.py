import datetime

from enums import AccountType, AccountStatus
from pydantic import BaseModel


class Account(BaseModel):
    """
    Схема данных счёта
    """

    id: int
    type: AccountType
    name: str
    status: AccountStatus
    opened: datetime.datetime
    closed: datetime.datetime
