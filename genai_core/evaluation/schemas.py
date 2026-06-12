from pydantic import BaseModel

class EvaluationResult(BaseModel):

    metric_name: str
    score: float