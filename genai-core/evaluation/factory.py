from .evaluators.qa_evaluator import QAEvaluator
from .metrics.bleu import BleuMetric
from .metrics.rouge import RougeMetric
from .metrics.bertscore import BERTScoreMetric

class EvaluatorFactory:

    @staticmethod
    def create(
        evaluation_type
    ):
        
        if evaluation_type == 'qa':
            
            return QAEvaluator(
                metrics=[
                    BleuMetric(),
                    RougeMetric(),
                    BERTScoreMetric()
                ]
            )
        
        raise ValueError(
            f"Unsupported Evaulator {evaluation_type}"
        )