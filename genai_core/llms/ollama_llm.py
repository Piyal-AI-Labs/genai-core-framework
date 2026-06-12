import ollama
from .base import BaseLLM

class OllamaLLM(BaseLLM):

    def __init__(
        self,
        model: str
    ):
        self.model = model

    def generate(
        self,
        prompt: str,
        **kwargs
    ) -> str:
        response = ollama.chat(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]