import asyncio
import logging
from datetime import datetime
from typing import List

from fastapi import FastAPI

from schemas.tinkoff_accounts_schema import Account
from tinkoff_client import TinkoffClient


logging.basicConfig(level=logging.DEBUG)

app = FastAPI()


# tc = TinkoffClient()


@app.get("/")
async def read_root() -> List[Account]:
    """
    Корневой элемент, основная "страница"
    :return: список счетов
    :rtype: List[Account]
    """

    accounts = []
    async with TinkoffClient() as tc:
        accounts = await tc.get_accounts()

    return accounts


@app.get("/accounts/{account_id}")
async def get_portfolio(account_id: str) -> List[dict]:
    """
    Список инструментов (ценных бумаг, валюты) для указанного счёта
    :param account_id: ID счёта
    :type account_id: str
    :return: список ЦБ, валюты
    :rtype: List[Instrument]
    """

    try:
        portfolio = []
        async with TinkoffClient() as tc:
            portfolio = await tc.get_portfolio(account_id)

            for position in portfolio:
                figi = position.get('figi')
                instrument_info = await tc.get_instrument_info(figi=figi)
                operations = await tc.get_operations(account_id,
                                                     datetime(datetime.now().year, 1, 1, 0, 0, 0, 0),
                                                     datetime.now(),
                                                     figi=figi)

                position['instrument_info'] = instrument_info
                position['operations'] = operations
        return portfolio
    except Exception as ex:
        logging.error(ex)


if __name__ == '__main__':
    asyncio.run(get_portfolio('2099628725'))
