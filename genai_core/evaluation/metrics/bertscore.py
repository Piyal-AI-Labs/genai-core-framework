from bert_score import score
from ..base import BaseMetric

class BERTScoreMetric(BaseMetric):

    def compute(
        self,
        predictions,
        references
    ):
        
        _, _, f1 = score(predictions, references, lang='en')

        return float(f1.mean())