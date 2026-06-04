from pydantic import BaseModel

class GenerationConfig(BaseModel):

    temperature: float = 0.7
    max_tokens: int = 1000
    top_p: float = 1.0