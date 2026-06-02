from abc import ABC, abstractmethod

class BaseEmbedding(ABC):

    @abstractmethod
    def embed_text(
        self,
        text: str
    ) -> list[float]:
        pass

    @abstractmethod
    def embed_document(
        self,
        texts: list[str]
    ) -> list[list[float]] :
        pass