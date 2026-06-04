from .openai_embedding import OpenAIEmbedding
from .sentence_embedding import SentenceEmbedding

class EmbeddingFactory:

    @staticmethod
    def create(
        provider: str,
        model: str,
        **kwargs
    ):
        
        if provider == "openai":
            return OpenAIEmbedding(
                model=model,
                api_key=kwargs['api_key']
            )
        
        if provider == "sentence_transformer":
            return SentenceEmbedding(
                model=model
            )
        
        raise ValueError(
            f"Unsupported provider: {provider}"
        )