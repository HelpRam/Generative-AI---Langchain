# Importing OpenAI class from langchain_openai
from langchain_openai import OpenAI  

# Importing load_dotenv to load environment variables from a .env file
from dotenv import load_dotenv  

# Loading environment variables (e.g., API keys) from the .env file
load_dotenv()  

# Initializing the OpenAI language model with a specified model version
llm = OpenAI(model='gpt-3.5-turbo-instruct')  

# Invoking the model with a query to get a response
result = llm.invoke("What is the capital of Nepal")  

# Printing the result returned by the model
print(result)  
