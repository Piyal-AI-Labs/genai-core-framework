from pydantic import BaseModel

class EmbeddingConfig(BaseModel):
    provider: str
    model: str
    batch_size: int = 32