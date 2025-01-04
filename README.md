

```markdown
# LangChain and OpenAI: A Comprehensive Guide

This repository demonstrates how to effectively use LangChain with OpenAI for various tasks such as language translation, tool integration, data processing, and more. Each section of the guide is modular and divided into Python scripts for easier understanding and execution.

---

## Table of Contents
1. [Setup and Environment Variables](#setup-and-environment-variables)
2. [Basic LangChain Example](#basic-langchain-example)
3. [Agents and Tools](#agents-and-tools)
4. [Using Wikipedia](#using-wikipedia)
5. [Prompt Templates](#prompt-templates)
6. [Chains](#chains)
7. [Conversation Memory](#conversation-memory)
8. [Accessing CSV Files](#accessing-csv-files)

---

## Setup and Environment Variables

Before running the scripts, ensure you have the following API keys:

- OpenAI API Key: `OPENAI_API_KEY`
- Hugging Face API Key: `HUGGINGFACEHUB_API_TOKEN`
- SERPAPI Key: `SERPAPI_API_KEY`

Set these environment variables in your terminal or include them in a `.env` file for automatic loading.

---

## Basic LangChain Example

File: basic_langchain.py

This script demonstrates how to use LangChain with OpenAI for simple tasks like text translation. 

Example:
```python
text = "translate how old are you to pidgen ?"
print(llm.invoke(text))
```

---

## Agents and Tools

**File**: `Agent_&_Tools.py`

This script showcases how to use agents and tools such as SERPAPI (for Google Search) and mathematical computations.

Example:
```python
agent.run("What was the GDP of US in 2022 plus 5?")
```

---

## Using Wikipedia

**File**: `wikipedia_tools.py`

Integrates Wikipedia as a tool to answer questions using LangChain.

Example:
```python
agent.run("In what year was the film Departed with Leonardo DiCaprio released? What is this year raised to the 0.43 power?")
```

---

## Prompt Templates

**File**: `prompt_templates.py`

Demonstrates how to create and use prompt templates for flexible and reusable prompts.

Example:
```python
prompt = PromptTemplate(
    template="Tell me a {adjective} joke",
    input_variables=["adjective"],
)
print(prompt.format(adjective="funny"))
```

---

## Chains

**File**: `chains.py`

Explains two ways to create chains in LangChain: standalone and combined.

Example 1:
```python
prompt = PromptTemplate(
    template="I want to open a restaurant for {cuisine} food. Suggest a fancy name for this.",
    input_variables=["cuisine"],
)
name_chain = LLMChain(llm=llm, prompt=prompt)
response = name_chain.run("Italian")
print(response)
```

Example 2:
```python
chain = SequentialChain(
    chains=[food_items_chain, name_chain],
    output_variables=['music_type', "country", "musician_names"],
    input_variables=['music_type']
)
print(chain({"music_type": "Afro beat"}))
```

---

## Conversation Memory

**File**: `conversation_memory.py`

Illustrates how to create a conversational agent with memory to retain context across interactions.

Example:
```python
convo.invoke("My name is Abdulmujeeb and I am the CTO of DYNAI.")
print(convo.invoke("Who is the CTO of DYNAI?")["response"])
```

---

## Accessing CSV Files

**File**: `csv_access.py`

Demonstrates how to integrate LangChain with pandas and a SQL database to query and analyze CSV data.

Example:
```python
agent_executor.invoke({"input": "How many people have more than 3 siblings?"})
```

---

## How to Run the Scripts

1. Clone this repository:
   ```bash
   git clone https://github.com/your-repo/langchain-guide.git
   cd langchain-guide
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the script of your choice:
   ```bash
   python Agent_&_Tools.py
   ```

---



## Contributing

If you find a bug or want to suggest an improvement, feel free to open an issue or submit a pull request.

Happy coding! 🚀
```

This **README.md** file is designed to be beginner-friendly and modular for easy navigation and understanding. Let me know if you'd like further adjustments!
