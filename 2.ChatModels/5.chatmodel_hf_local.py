# Importing necessary classes from langchain_huggingface
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

# Initializing the Hugging Face pipeline with a specific model
# - model_id: Specifies the Hugging Face model to use (TinyLlama-1.1B-Chat-v0.1)
# - task: Defines the type of task the model will perform (text-generation)
# - pipeline_kwargs: Additional parameters like temperature and max tokens for response control
llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v0.1",  # Correct model ID
    task="text-generation",  # Ensure no extra spaces
    pipeline_kwargs=dict(
        temperature=0.5,  # Controls randomness (higher = more creative responses)
        max_new_tokens=100  # Limits the maximum tokens in the generated response
    )
)

# Wrapping the model in ChatHuggingFace for a chat-like interaction
model = ChatHuggingFace(llm=llm)

# Invoking the model with a query to get the response
result = model.invoke("What is the capital of Nepal?")

# Printing the generated response
print(result.content)
