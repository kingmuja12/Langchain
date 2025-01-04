################## Prompt ################\
from langchain_core.prompts import PromptTemplate
prompt = PromptTemplate(
    template="Tell me a {adjective} joke",
    input_variables=["adjective"],
)

out_come = prompt.format(adjective="funny")

print(out_come)