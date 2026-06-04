from openai import OpenAI
from .base import BaseEmbedding

class OpenAIEmbedding(BaseEmbedding):

    def __init__(
        self,
        model: str,
        api_key: str
    ):
        self.model = model
        self.client = OpenAI(
            api_key=api_key
        )

    def embed_text(
        self,
        text: str
    ):
        response = self.client.embeddings.create(
            model=self.model,
            input=text
        )

        return response.data[0].embedding
    
    def embed_document(
        self,
        texts: list[str]
    ):
        
        response = self.client.embeddings.create(
            model=self.model,
            input=texts
        )

        return [
            item.embedding for item in response.data
        ]