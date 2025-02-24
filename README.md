# Pandas DataFrame Agent with Pydantic-AI

This repository contains a Python script that uses `pydantic-ai` to create an AI agent capable of querying a pandas DataFrame. This agent is designed to answer questions about data stored in a CSV file by executing pandas `eval` queries.

## Prerequisites

Before running the script, ensure you have the following:

*   **Python 3.7+**
*   **A Groq API Key**: You need an API key from Groq to use their models. You can sign up and get an API key at [GroqCloud](https://console.groq.com/).
*   **Poetry** (Optional but Recommended): For managing dependencies and virtual environment. If you don't have Poetry, you can use `pip` and `venv` instead.

## Setup and Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/ramin4251/Pandas-DataFrame-Agent-with-Pydantic-AI
    cd Pandas-DataFrame-Agent-with-Pydantic-AI
    ```

2.  **Set up your virtual environment and install dependencies:**

    **Using Poetry (Recommended):**

    ```bash
    poetry install
    ```

    **Using pip and venv:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    pip install -r requirements.txt
    ```

3.  **Create a `.env` file:**

    Make an empty `.env` file and replace `YOUR_GROQ_API_KEY` with actual Groq API key.

    ```
    GROQ_API_KEY=YOUR_GROQ_API_KEY
    ```

## Usage

1.  **Run the script:**

    ```bash
    python pandas_df_agent.py
    ```

    The script will load the `sampleCSV2.csv` file and ask the agent a few example questions. You can modify the `ask_agent()` calls at the end of the script to ask your own questions.

## Example Questions in the script:

*   What are the column names in this dataset?
*   How many rows are in this dataset?
*   What are unique values in column: zone?

## Understanding the Code

*   **`pandas_df_agent.py`**: This is the main Python script. It defines a `Deps` dataclass to hold the pandas DataFrame, sets up the `pydantic-ai` Agent, defines the `df_query` tool, and includes example questions.
*   **`sampleCSV2.csv`**: This is a sample CSV file used for demonstration. You can replace this with your own CSV data.
*   **`df_query` tool**: This tool is the core of the agent. It allows the agent to execute pandas `eval` queries on the DataFrame. The agent will use this tool to answer your questions about the data.

## Contributing

Feel free to contribute to this project by opening issues or submitting pull requests.

