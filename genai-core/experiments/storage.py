import json
from pathlib import Path
from .schemas import ExperimentResult

class ExperimentStorage:

    def __init__(
        self,
        experiment_dir: str = "experiments"
    ):
        
        self.experiment_dir = Path(experiment_dir)

        self.experiment_dir.mkdir(parents=True, exist_ok=True)


    def save(
        self,
        result: ExperimentResult
    ):
        
        filepath = (
            self.experiment_dir / f"{result.experiment_id}.json"
        )

        with open(
            filepath, "w", encoding="utf-8"
        ) as f:
            
            json.dump(
                result.model_dump(
                    mode="json"
                ),
                f,
                indent=4
            )

    def load (
        self,
        experiment_id: str
    ):
        
        filepath = (
            self.experiment_dir / f"{experiment_id}.json"
        )

        with open(
            filepath,
            "r",
            encoding="utf-8"
        ) as f:
            
            data = json.load(f)

        return ExperimentResult(**data)
    