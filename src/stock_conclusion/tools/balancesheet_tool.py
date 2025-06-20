from crewai.tools import BaseTool
from typing import Type

from pandas import DataFrame
from pydantic import BaseModel, Field

import yfinance as yf


class BalanceSheetInput(BaseModel):
    ticker: str

class BalanceSheet(BaseTool):
    name: str = "BalanceSheet"
    description: str = (
        "Useful to get the balance sheet of a company. The input should be a ticker, for example AAPL, NET."
    )
    args_schema: Type[BaseModel] = BalanceSheetInput

    def _run(self, ticker: str) -> DataFrame:
        try:
            ticker = yf.Ticker(ticker)
            return ticker.balance_sheet
        except Exception as e:
            raise f"[Error fetching Gather Balance Sheet]: {str(e)}"
