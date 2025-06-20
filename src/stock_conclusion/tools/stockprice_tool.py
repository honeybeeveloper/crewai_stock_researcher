from crewai.tools import BaseTool
from typing import Type

from pandas import DataFrame
from pydantic import BaseModel, Field

import yfinance as yf


class StockPriceToolInput(BaseModel):
    ticker: str

class StockPriceTool(BaseTool):
    name: str = "StockPrice"
    description: str = (
        "Get the exact stock price. The input should be a ticker, for example AAPL, NET."
    )
    args_schema: Type[BaseModel] = StockPriceToolInput

    def _run(self, ticker: str) -> DataFrame:
        try:
            ticker = yf.Ticker(ticker)
            return ticker.history(period="1mo")
        except Exception as e:
            raise f"[Error fetching Stock Price]: {str(e)}"
