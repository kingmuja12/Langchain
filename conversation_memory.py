################# Memory (using the type of conversation memory where by it can remember the amount of information you spicify) ##############
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferWindowMemory
from langchain_openai import OpenAI

llm = OpenAI(temperature=0)
memory = ConversationBufferWindowMemory(k=15) ### since k is equal to 15 then it can remember the last 15 conversation that we are having

convo = ConversationChain(
    llm=OpenAI(temperature=0.7),
    memory=memory
)

# Use case: This functionality could also be implemented using a while loop 
# to enable continuous conversations.
# Note: Since k = 15, the system is designed to retain memory of only the last 15 messages.
convo.invoke("my name is Abdulmujeeb and i am the CTO of DYNAI")

print(convo.invoke("who is the CTO of DYNAI")["response"]) ### this prints out the response
