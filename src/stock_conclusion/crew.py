from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators


import yfinance as yf
from crewai_tools import ScrapeWebsiteTool
from crewai.tools import tool

import logging

logging.basicConfig(
    filename="crewai.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger()
logger.setLevel(logging.INFO)


@CrewBase
class StockConclusion():
    """StockConclusion crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    scrape_tool = ScrapeWebsiteTool()

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'], # type: ignore[index]
            verbose=True,
            tools=[
                self.scrape_tool,
                stock_news,
            ],
        )

    @agent
    def technical_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['technical_analyst'], # type: ignore[index]
            verbose=True, 
            tools=[
                stock_price
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
                insider_transactions
            ] 
        )
    
    @agent
    def hedge_fund_manager(self) -> Agent:
        return Agent(
            config=self.agents_config['hedge_fund_manager'], # type: ignore[index]
            verbose=True
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def research(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'], # type: ignore[index]
        )

    @task
    def technical_analysis(self) -> Task:
        return Task(
            config=self.tasks_config['technical_analyst_task'], # type: ignore[index]
            output_file='technical_analyst_output.md'
        )

    @task
    def financial_analysis(self) -> Task:
        return Task(
            config=self.tasks_config['financial_analyst_task'], # type: ignore[index]
            output_file='financial_analyst_output.md'
        )
    
    @task
    def investment_recommendation(self) -> Task:
        return Task(
            config=self.tasks_config['hedge_fund_manager_task'], # type: ignore[index]
            output_file='hedge_fund_manager_output.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the StockConclusion crew"""

        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )

@tool("Stock News")
def stock_news(ticker):
    """
    Useful to get news about a stock.
    The input should be a ticker, for example AAPL, NET.
    """
    try:
        print(f'ticker : {ticker}')
        ticker = yf.Ticker(ticker)
        print(f'ticker : {ticker}')
        return ticker.news
    except Exception as e:
        logger.debug(str(e))
        raise f"[Error fetching Stock News]: {str(e)}"


@tool("Stock Price")
def stock_price(ticker):
    """
    Get the exact stock price.
    The input should be a ticker, for example AAPL, NET.
    """
    try:
        ticker = yf.Ticker(ticker)
        print(f'ticker : {ticker}')
        return ticker.history(period="1mo")
    except Exception as e:
        raise Exception(f"An error occurred from stock_price: {e}")

@tool("Income Statement")
def income_stmt(ticker):
    """
    Useful to get the income statement of a company.
    The input should be a ticker, for example AAPL, NET.
    """
    try:
        ticker = yf.Ticker(ticker)
        return ticker.income_stmt
    except Exception as e:
        raise Exception(f"An error occurred from income_stmt: {e}")


@tool("Balance Sheet")
def balance_sheet(ticker):
    """
    Useful to get the balance sheet of a company.
    The input should be a ticker, for example AAPL, NET.
    """
    try:
        ticker = yf.Ticker(ticker)
        return ticker.balance_sheet
    except Exception as e:
        raise Exception(f"An error occurred from balance_sheet: {e}")

@tool("Insider Transactions")
def insider_transactions(ticker):
    """
    Useful to get the insider transactions of a stock.
    The input should be a ticker, for example AAPL, NET.
    """
    try:
        ticker = yf.Ticker(ticker)
        return ticker.insider_transactions
    except Exception as e:
        raise Exception(f"An error occurred from insider_transactions: {e}")