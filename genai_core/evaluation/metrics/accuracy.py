from sklearn.metrics import accuracy_score
from ..base import BaseMetric

class AccuracyMetric(BaseMetric):

    def compute(
        self,
        predictions,
        references
    ):
        
        return accuracy_score(
            references,
            predictions
        )