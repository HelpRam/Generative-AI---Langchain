from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


# Initialize the embedding model using the Sentence Transformers model
embedding = HuggingFaceEmbeddings(model_name=("sentence-transformers/all-MiniLM-L6-v2"))

# Define the input text for embedding
documents = [
    "Kathmandu is the capital of Nepal",
    "Pokhara is a beautiful city in Nepal",
    "Paris is the capital of France",
    "delhi is the capital of india",
    "dhaka is the capital of bangladesh"
]

query = " what is capital of Nepal"

doc_embedding = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

score = cosine_similarity([query_embedding], doc_embedding)[0]

index,score = sorted(list(enumerate(score)),key = lambda x:x[1]) [-1]

print(query)
print(documents[index])
print("similarity score is ", score)