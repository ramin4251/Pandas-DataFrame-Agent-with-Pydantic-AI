
from dotenv import load_dotenv
import os
import pandas as pd
from dataclasses import dataclass

from pydantic_ai import Agent, RunContext, ModelRetry

# Apply `nest_asyncio` to avoid errors when running asyncio code in a Jupyter notebook.
# This prevents `event loop is already running` errors by allowing nested event loops.
import nest_asyncio

nest_asyncio.apply()

load_dotenv(dotenv_path=r'.env')
groq_api_key = os.getenv("GROQ_API_KEY")
os.environ['GROQ_API_KEY'] = groq_api_key
os.environ['LOGFIRE_IGNORE_NO_CONFIG'] = '1'

csv_file_path = r'./sampleCSV2.csv'
df = pd.read_csv(csv_file_path)


@dataclass
class Deps:
    """The only dependency we need is the DataFrame we'll be working with."""
    df: pd.DataFrame


MODEL_LIST = [
    "gemma2-9b-it",
    "llama-3.3-70b-specdec",
    "deepseek-r1-distill-llama-70b",
    "qwen-2.5-32b",
    "deepseek-r1-distill-qwen-32b",
    "mixtral-8x7b-32768",
]

agent = Agent(
    model='groq:gemma2-9b-it',
    system_prompt="""You are an AI assistant that helps extract information from a pandas DataFrame.
    If asked about columns, be sure to check the column names first.
    Be concise in your answers.""",
    deps_type=Deps,
    retries=10,
)


@agent.tool
async def df_query(ctx: RunContext[Deps], query: str) -> str:
    """A tool for running queries on the `pandas.DataFrame`. Use this tool to interact with the DataFrame.
    `query` will be executed using `pd.eval(query, target=df)`, so it must contain syntax compatible with
    `pandas.eval`.
    """

    # Print the query for debugging purposes and fun :)
    print(f'Running query: `{query}`')
    try:
        # Execute the query using `pd.eval` and return the result as a string (must be serializable).
        return str(pd.eval(query, target=ctx.deps.df))
    except Exception as e:
        #  On error, raise a `ModelRetry` exception with feedback for the agent.
        raise ModelRetry(f'query: `{query}` is not a valid query. Reason: `{e}`') from e


def ask_agent(question):
    """Function to ask questions to the agent and display the response"""
    deps = Deps(df=df)
    print(f"Question: {question}")
    response = agent.run_sync(question, deps=deps)
    print(f"Answer: {response.new_messages()[-1].parts[0].content}")
    print("---")


# Example questions
ask_agent("What are the column names in this dataset?")
ask_agent("How many rows are in this dataset?")
ask_agent("What are unique values in column: zone?")


