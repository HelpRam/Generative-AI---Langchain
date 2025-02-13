# Importing ChatHuggingFace and HuggingFaceEndpoint from langchain_huggingface  
# - ChatHuggingFace is used to interact with Hugging Face models in a chat-like manner  
# - HuggingFaceEndpoint allows connecting to Hugging Face-hosted models  
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint  

# Importing load_dotenv to load environment variables from a .env file  
from dotenv import load_dotenv  

# Loading environment variables (e.g., API keys for Hugging Face) from the .env file  
load_dotenv()  

# Initializing the Hugging Face model endpoint  
# - repo_id: Specifies the Hugging Face model to use (TinyLlama-1.1B-Chat-v0.1)  
# - task: Defines the type of task the model will perform (text-generation in this case)  
llm = HuggingFaceEndpoint(  
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v0.1",  
    task="text-generation"  
)  

# Wrapping the model in ChatHuggingFace for chat-like interactions  
model = ChatHuggingFace(llm=llm)  

# Invoking the model with a query to generate text about Nepal  
result = model.invoke("write about Nepal")  

# Printing the generated response  
print(result)  
