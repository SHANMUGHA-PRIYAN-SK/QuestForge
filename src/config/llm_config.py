import json
from dotenv import load_dotenv
import os
from langchain_huggingface import HuggingFaceEndpoint
# Load .env file
load_dotenv()
# Hugging Face API Key and Endpoint Setup
repo_key = os.getenv("HUGGINGFACE_TOKEN")

repo_id = "deepseek-ai/DeepSeek-V3-0324"  # Hugging Face endpoint repository ID
llm = HuggingFaceEndpoint(
    repo_id=repo_id,
    temperature=0.7,  # Increased for more creative quests
    task="text-generation",
    model_kwargs={
        "token": repo_key,
        "max_tokens": 100  # Increased for longer quest descriptions
    }
)

print(llm.invoke("Hello, how are you?"))