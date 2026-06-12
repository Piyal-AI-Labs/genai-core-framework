from datetime import datetime, timezone
from typing import Any
from pydantic import BaseModel, Field

class ExperimentResult(BaseModel):

    experiment_id: str
    experiment_name: str
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )
    parameters: dict[str, Any] = {}
    metrics: dict[str, float] = {}
    metadata: dict[str, Any] = {}