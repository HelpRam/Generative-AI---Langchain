# Importing ChatAnthropic from langchain_anthropic to interact with Anthropic's Claude models
from langchain_anthropic import ChatAnthropic  

# Importing load_dotenv to load environment variables from a .env file
from dotenv import load_dotenv  

# Loading environment variables (e.g., API keys) from the .env file
load_dotenv()  

# Initializing the ChatAnthropic model with a specified version
# - model: Specifies the Claude model to use (claude-3.5-sonnet-20241022 in this case)
model = ChatAnthropic(model="claude-3.5-sonnet-20241022")  

# Invoking the model with a query and storing the response
result = model.invoke("What is the capital of Nepal")  

# Printing the content of the response returned by the model
print(result.content)  
