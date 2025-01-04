import os
from langchain_openai import OpenAI

### These are just examples using langchain with Open ai

os.environ['OPENAI_API_KEY'] = "PUT YOUR API"

os.environ["HUGGINGFACEHUB_API_TOKEN"] = "PUT YOUR API"

llm = OpenAI(temperature=0.6)
text="translate how old are you to pidgen ?"
print(llm.invoke(text))