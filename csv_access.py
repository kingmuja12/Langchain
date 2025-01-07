 ### how to access CSV files using open ai, langchain and pandas



import pandas as pd
url = "https://raw.githubusercontent.com/sudarshan-koirala/Logistic-Regression-for-Titanic-Dataset/master/Train_Titanic.csv"
df = pd.read_csv(url)
# print(df.shape)
# print(df.columns.tolist())
# print(df.head())

## Now we want our agent to be able to access our csv file
from langchain_community.utilities import SQLDatabase
from sqlalchemy import create_engine

engine = create_engine("sqlite:///titanic.db")

db = SQLDatabase(engine=engine)
from langchain_community.agent_toolkits import create_sql_agent
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
agent_executor = create_sql_agent(llm, db=db, agent_type="openai-tools", verbose=True)
agent_executor.invoke({"input": "How many people have more than 3 siblings"})