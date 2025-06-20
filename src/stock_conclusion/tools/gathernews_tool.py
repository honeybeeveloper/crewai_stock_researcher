from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field

import yfinance as yf


class GatherNewsToolInput(BaseModel):
    ticker: str

class GatherNewsTool(BaseTool):
    name: str = "GatherNews"
    description: str = (
        "Useful to get news about a company. The input should be a ticker, for example AAPL, NET."
    )
    args_schema: Type[BaseModel] = GatherNewsToolInput

    def _run(self, ticker: str) -> list:
        try:
            ticker = yf.Ticker(ticker)
            return ticker.news
        except Exception as e:
            raise f"[Error fetching Gather News]: {str(e)}"
