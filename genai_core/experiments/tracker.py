import uuid
from .schemas import ExperimentResult
from .storage import ExperimentStorage

class ExperimentTracker:

    def __init__(
        self,
        experiment_name: str
    ):
        
        self.result = ExperimentResult(
            experiment_id=str(uuid.uuid4),
            experiment_name=experiment_name
        )

        self.storage = ExperimentStorage()

    def log_param(
        self,
        key,
        value
    ):
        
        self.result.parameters[key] = value
    
    def log_params(
        self,
        params: dict
    ):
        for key, value in params.items():
            self.log_param(key, value)

    def log_metric(
        self,
        key,
        value
    ):
        
        self.result.metrics[key] = value

    def log_metrics(
        self,
        metrics: dict
    ):
        for key, value in metrics.items():
            self.log_metric(key, value)

    def log_metadata(
        self,
        key,
        value
    ):
        
        self.result.metadata[key] = value

    def save(self):

        self.storage.save(
            self.result
        )