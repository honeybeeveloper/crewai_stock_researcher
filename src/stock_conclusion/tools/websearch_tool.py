from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field

import requests
from bs4 import BeautifulSoup # crawling lib



class WebSearchToolInput(BaseModel):
    """Input schema for MyCustomTool."""
    query: str
    limit: int = 5

class WebSearchTool(BaseTool):
    name: str = "WebSearchTool"
    description: str = (
        "Performs a simple DuckDuckGo web search and returns top results."
    )
    args_schema: Type[BaseModel] = WebSearchToolInput

    def _run(self, query: str) -> str:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }
        search_url = f"https://html.duckduckgo.com/html/?q={query}"
        response = requests.get(search_url, headers=headers)

        if response.status_code != 200:
            return "Search failed."

        soup = BeautifulSoup(response.text, "html.parser")
        results = soup.find_all("a", class_="result__a", limit=5)

        output = "Top search results:\n"
        for i, result in enumerate(results, 1):
            title = result.get_text()
            link = result.get("href")
            output += f"{i}. {title}\n   {link}\n"

        return output
