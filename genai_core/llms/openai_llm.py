from openai import OpenAI
from .base import BaseLLM

class OpenAILLM(BaseLLM):

    def __init__(
        self,
        model: str,
        api_key: str
    ):
        self.model = model
        self.client = OpenAI(
            api_key=api_key
        )

    def generate(
        self, 
        prompt: str, 
        **kwargs
    )-> str:
        
        response = self.client.responses.create(
            model = self.model,
            input = prompt
        )

        return response.output_text