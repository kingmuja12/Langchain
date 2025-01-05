################# CHAINS ##############
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_openai import OpenAI


llm = OpenAI(temperature=0.5)
############## Two ways to use chain ####################
## First way:
prompt = PromptTemplate(
    template="I want to open a restaurant for {cuisine} food. Suggest a fency name for this.",
    input_variables=["cuisine"],
)
name_chain = LLMChain(llm = llm, prompt = prompt)
response= name_chain.run("restaurant_name")
print(response)

## Second way:
prompt2 = PromptTemplate.from_template("Suggest some menu items for {restaurant_name}") 
chain = LLMChain(llm = llm, prompt = prompt2)
# response1= chain.run("restaurant_nam")
# print(response1)

############## Combine chain method ############
prompt = PromptTemplate(
    template="give me the name of the musicians in  {country} ",
    input_variables=["country"],
)
name_chain = LLMChain(llm = llm, prompt = prompt, output_key = "musician_names")

prompt_template_items = PromptTemplate(
    input_variables = ['music_type'],
    template="tell me the country name that does this type of music {music_type}."
)

food_items_chain =LLMChain(llm=llm, prompt=prompt_template_items, output_key="country")

from langchain.chains import SequentialChain

chain = SequentialChain(
    chains = [food_items_chain, name_chain], #### this are the chains you created 
    output_variables = ['music_type', "country", "musician_names"], ####this is what you want it to print out as the final code 
    input_variables = ['music_type'] ### this the parameter that you will pass in to it for excussion purpose 
)
# print(chain({"music_type": "Afro beat"}))
