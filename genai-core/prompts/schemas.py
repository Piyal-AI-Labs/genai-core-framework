from pydantic import BaseModel

class PromptTemplate(BaseModel):
    name: str
    content: str