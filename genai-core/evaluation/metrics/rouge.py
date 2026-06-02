from rouge_score import rouge_scorer
from ..base import BaseMetric

class RougeMetric(BaseMetric):

    def compute(
        self,
        predictions,
        references
    ):
        scorer = rouge_scorer.RougeScorer(
            ["rouge1"],
            use_stemmer = True
        )

        scores = []

        for pred, ref in zip(predictions, references):

            score = scorer.score(
                ref, pred
            )

            scores.append(
                score['rouge1'].fmeasure
            )

            return sum(scores) / len(scores)