# Importing ChatOpenAI from langchain_openai for interacting with OpenAI's chat models
from langchain_openai import ChatOpenAI  

# Importing load_dotenv to load environment variables from a .env file
from dotenv import load_dotenv  

# Loading environment variables (e.g., API keys) from the .env file
load_dotenv()  

# Initializing the ChatOpenAI model with specified parameters
# - model: Specifies the OpenAI model to use (gpt-4 in this case)
# - temperature: Controls randomness; lower values make responses more deterministic
# - max_completion_tokens: Limits the number of tokens in the response
model = ChatOpenAI(model="gpt-4", temperature=0.7, max_completion_tokens=10)  

# Invoking the model with a query and storing the response
result = model.invoke("What is the capital of Nepal")  

# Printing the content of the response returned by the model
print(result.content)  
