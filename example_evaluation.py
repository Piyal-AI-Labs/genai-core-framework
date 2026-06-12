from genai_core.evaluation.factory import EvaluatorFactory

predictions = [
    "Paris is the capital city of France"
]

references = [
    "The capital of France is Paris"
]

evaluator = EvaluatorFactory.create("qa")

results = evaluator.evaulate(predictions, references)

print(results)