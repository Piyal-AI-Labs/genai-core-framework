from .openai_llm import OpenAILLM
from .ollama_llm import OllamaLLM

class LLMFactory:

    @staticmethod
    def create(
        provider:str,
        model: str,
        **kwargs
    ):
        if provider == "openai":
            return OpenAILLM(
                model=model,
                api_key=kwargs['api_key']
            )

        if provider == "ollama":
            return OllamaLLM(
                model=model
            )

        raise ValueError(
            f"Unsupported provider: {provider}"
        )