from genai_core.embeddings.factory import EmbeddingFactory
from dotenv import load_dotenv
import os

load_dotenv()

embedding = EmbeddingFactory.create(
    provider="openai",
    model="text-embedding-3-small",
    api_key=os.environ.get("OPENAI_API_KEY")
)

vector = embedding.embed_text(
    "What is RAG?"
)

print(len(vector))