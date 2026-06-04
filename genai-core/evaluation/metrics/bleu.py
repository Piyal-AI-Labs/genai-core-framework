from nltk.translate.bleu_score import (
    sentence_bleu
)
from ..base import BaseMetric

class BleuMetric(BaseMetric):

    def compute(
        self,
        predictions,
        refernecs
    ):
        
        scores = []

        for pred, ref in zip(predictions, refernecs):
            score = sentence_bleu(
                [ref.split()],
                pred.split()
            )

            scores.append(score)

        return sum(scores) / len(scores)