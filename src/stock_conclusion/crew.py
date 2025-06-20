from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List


import datetime
from crewai_tools import ScrapeWebsiteTool

from stock_conclusion import app_config
from stock_conclusion.tools.websearch_tool import WebSearchTool
from stock_conclusion.tools.sentimentanalysis_tool import SentimentAnalysisTool

from stock_conclusion.tools import BalanceSheet, GatherNewsTool, IncomeStatementTool, InsiderTransaction, StockPriceTool


now_str = datetime.datetime.now().strftime('%y%m%d_%H%M%S')

# Tool Instance
scrape_tool = ScrapeWebsiteTool()
web_search_tool = WebSearchTool()
sentiment_analysis_tool = SentimentAnalysisTool()
stock_news = GatherNewsTool()
stock_price = StockPriceTool()
income_stmt = IncomeStatementTool()
balance_sheet = BalanceSheet()
insider_transactions = InsiderTransaction()


@CrewBase
class StockConclusion():
    """StockConclusion crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    company = app_config.company


    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'], # type: ignore[index]
            verbose=True,
            tools=[
                scrape_tool,
                web_search_tool,
                stock_news,
            ],
        )

    @agent
    def technical_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['technical_analyst'], # type: ignore[index]
            verbose=True, 
            tools=[
                stock_price,
            ]
        )
    
    @agent
    def financial_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['financial_analyst'], # type: ignore[index]
            verbose=True,
            tools=[
                income_stmt,
                balance_sheet,
                insider_transactions,
            ] 
        )

    @agent
    def sentiment_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['sentiment_analyst'],  # type: ignore[index]
            verbose=True,
            tools=[
                sentiment_analysis_tool,
            ]
        )
    
    @agent
    def fund_manager(self) -> Agent:
        return Agent(
            config=self.agents_config['fund_manager'], # type: ignore[index]
            verbose=True
        )

    @task
    def research(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'], # type: ignore[index]
        )

    @task
    def technical_analysis(self) -> Task:
        return Task(
            config=self.tasks_config['technical_analysis_task'], # type: ignore[index]
            context=[self.research()],
            output_file = f"{self.company}_technical_analysis_{now_str}.md",
        )

    @task
    def financial_analysis(self) -> Task:
        return Task(
            config=self.tasks_config['financial_analysis_task'], # type: ignore[index]
            context=[self.research()],
            output_file=f"{self.company}_financial_analysis_{now_str}.md",
        )

    @task
    def sentiment_analysis(self) -> Task:
        return Task(
            config=self.tasks_config['sentiment_analysis_task'],  # type: ignore[index]
            output_file=f"{self.company}_sentiment_analysis_{now_str}.md",
        )
    
    @task
    def investment_decision(self) -> Task:
        return Task(
            config=self.tasks_config['stock_decision_task'], # type: ignore[index]
            context=[self.technical_analysis(), self.financial_analysis(), self.sentiment_analysis()],
            output_file=f"{self.company}_investment_decision_{now_str}.md",
        )

    @crew
    def crew(self) -> Crew:
        """Creates the StockConclusion crew"""
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical
        )