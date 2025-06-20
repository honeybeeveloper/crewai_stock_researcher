from crewai.tools import BaseTool
from typing import Type

from pandas import DataFrame
from pydantic import BaseModel, Field

import yfinance as yf


class IncomeStatementToolInput(BaseModel):
    ticker: str

class IncomeStatementTool(BaseTool):
    name: str = "IncomeStatement"
    description: str = (
        "Useful to get the income statement of a company. The input should be a ticker, for example AAPL, NET."
    )
    args_schema: Type[BaseModel] = IncomeStatementToolInput

    def _run(self, ticker: str) -> DataFrame:
        try:
            ticker = yf.Ticker(ticker)
            return ticker.income_stmt
        except Exception as e:
            raise f"[Error fetching Income Statement]: {str(e)}"
