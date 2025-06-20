from crewai.tools import BaseTool
from typing import Type

from pandas import DataFrame
from pydantic import BaseModel, Field

import yfinance as yf


class InsiderTransactionInput(BaseModel):
    ticker: str

class InsiderTransaction(BaseTool):
    name: str = "InsiderTransaction"
    description: str = (
        "Useful to get the insider transactions of a stock. The input should be a ticker, for example AAPL, NET."
    )
    args_schema: Type[BaseModel] = InsiderTransactionInput

    def _run(self, ticker: str) -> DataFrame:
        try:
            ticker = yf.Ticker(ticker)
            return ticker.insider_transactions
        except Exception as e:
            raise f"[Error fetching Insider Transaction]: {str(e)}"
