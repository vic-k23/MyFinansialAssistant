import datetime

from pydantic import BaseModel

from enums import AccountType, AccountStatus


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
