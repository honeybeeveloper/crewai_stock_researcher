#!/usr/bin/env python
import sys
import warnings

from stock_conclusion import app_config
from stock_conclusion.crew import StockConclusion

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'company' : app_config.company
    }
    
    try:
        StockConclusion().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {str(e)}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'company' : app_config.company
    }
    try:
        StockConclusion().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {str(e)}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        StockConclusion().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {str(e)}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
       'company' : app_config.company
    }
    
    try:
        StockConclusion().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {str(e)}")


if __name__ == '__main__':
    run()
