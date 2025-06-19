# Import the HuggingFaceEmbeddings class from LangChain
from langchain_huggingface import HuggingFaceEmbeddings

# Initialize the embedding model using the Sentence Transformers model
embedding = HuggingFaceEmbeddings(model_name=("sentence-transformers/all-MiniLM-L6-v2"))

# Define the input text for embedding
text = "Kathmandu is the capital of Nepal"

# Generate the embedding (vector representation) for the input text
Vector = embedding.embed_query(text)

# Print the vector as a string representation
print(str(Vector))
