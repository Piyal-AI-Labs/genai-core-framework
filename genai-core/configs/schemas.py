from pydantic import BaseModel, Field

class LLMConfig(BaseModel):

    provider: str
    model: str
    temperature: float = Field(default=0.7)
    max_tokens: int = Field(default=1000)

class EmbeddingConfig(BaseModel):
    provider: str
    model: str

class ExperimentConfig(BaseModel):
    name: str
    output_dir: str = "outputs"

class AppConfig(BaseModel):
    llm: LLMConfig
    embeddings: EmbeddingConfig
    experiment: ExperimentConfig