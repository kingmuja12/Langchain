### How to access CSV files using OpenAI, LangChain, and Pandas

# Importing necessary libraries
import pandas as pd  # For handling and analyzing data
import os  # For accessing environment variables

# Setting up the OpenAI API key (replace "Put your API key here" with your actual key)
os.environ['OPENAI_API_KEY'] = "Put your API key here"

# Define the URL of the CSV file 
url = ""

# Load the CSV file into a Pandas DataFrame
df = pd.read_csv(url)

# Display the shape (rows, columns) of the DataFrame
print(df.shape)

# Print the column names of the DataFrame
print(df.columns.tolist())

# Print the first few rows of the DataFrame
print(df.head())

## Now we want our agent to be able to access our CSV file

# Import SQLDatabase utility from LangChain Community and SQLAlchemy for database operations
from langchain_community.utilities import SQLDatabase
from sqlalchemy import create_engine

# Create an SQLite database engine (local database for demonstration)
engine = create_engine("sqlite:///titanic.db")

# Initialize a SQLDatabase object with the created SQLite engine
db = SQLDatabase(engine=engine)

# Import tools to create a LangChain SQL agent
from langchain_community.agent_toolkits import create_sql_agent
from langchain_openai import ChatOpenAI

# Initialize a ChatOpenAI object with the desired model and parameters
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

# Create an SQL agent that can interact with the database using the LLM
agent_executor = create_sql_agent(llm, db=db, agent_type="openai-tools", verbose=True)

# Provide an input query for the agent to process
# This query asks how many people in the dataset have more than 3 siblings
Input = agent_executor.invoke({"input": "How many people have more than 3 siblings"})

# Extract the output from the agent's response
Output = Input["output"]

# Print the result of the query
print(Output)
