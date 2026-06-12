class QAEvaluator:

    def __init__(
        self,
        metrics
    ):
        self.metrics = metrics

    def evaulate(
        self,
        predictions,
        references
    ):
        
        results = {}

        for metric in self.metrics:
            results[metric.__class__.__name__] = metric.compute(
                predictions, references
            )

        return results