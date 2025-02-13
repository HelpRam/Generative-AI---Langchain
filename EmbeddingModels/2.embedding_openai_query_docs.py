# Importing OpenAIEmbeddings from langchain_openai  
# - OpenAIEmbeddings is used to generate vector embeddings for text  
from langchain_openai import OpenAIEmbeddings  

# Importing load_dotenv to load environment variables from a .env file  
from dotenv import load_dotenv  

# Loading environment variables (e.g., API keys) from the .env file  
load_dotenv()  

# Initializing the OpenAI embeddings model  
# - model: Specifies the OpenAI embedding model ('text-embedding-3-large')  
# - dimensions: Defines the size of the output embedding vector (32 in this case)  
embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)  

documents = [
    "Kathmandu is the capital of Nepal",
    "Nepal is a landlocked country in south Asia"
    " nepal is known for mount everest and the himalayas"

]
# Generating an embedding vector for the given text query  
result = embedding.embed_query(documents)  

# Printing the generated embedding vector as a string  
print(str(result))  
