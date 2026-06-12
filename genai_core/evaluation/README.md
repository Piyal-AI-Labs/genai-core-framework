# Metrics Module (v1.0)

A simple collection of evaluation metrics for measuring the performance of Generative AI systems.

This module provides a unified interface for computing evaluation metrics across different tasks such as question answering, text generation, summarization, and semantic similarity evaluation.

The goal is to make evaluation consistent, reproducible, and reusable across all research projects within the Piyal-AI-Labs ecosystem.

---

## Features

### Supported Metrics

#### Traditional Metrics

* Accuracy

#### NLP Metrics

* BLEU
* ROUGE

#### Semantic Metrics

* BERTScore

---

## Why Use This Module?

Evaluation is one of the most important parts of AI research.

Without a common evaluation framework, different projects often use different implementations, making comparisons difficult.

This module provides a standard interface:

```python
metric = RougeMetric()

score = metric.compute(
    predictions,
    references
)
```

Every metric follows the same pattern, making it easy to swap metrics or evaluate multiple models using a consistent workflow.

---

## Module Structure

```text
evaluation/
│
├── metrics/
│   ├── accuracy.py
│   ├── bleu.py
│   ├── rouge.py
│   └── bertscore.py
│
├── evaluators/
│   └── qa_evaluator.py
│
├── factory.py
└── report.py
```

### accuracy.py

Implements classification accuracy.

### bleu.py

Implements BLEU score for text generation evaluation.

### rouge.py

Implements ROUGE score for summarization and text overlap evaluation.

### bertscore.py

Implements BERTScore for semantic similarity evaluation.

---

## Installation

Install the required dependencies:

```bash
pip install scikit-learn
pip install nltk
pip install rouge-score
pip install bert-score
```

---

## Common Interface

All metrics implement the same interface:

```python
score = metric.compute(
    predictions,
    references
)
```

### Parameters

| Parameter   | Type | Description                    |
| ----------- | ---- | ------------------------------ |
| predictions | list | Model-generated outputs        |
| references  | list | Ground-truth reference outputs |

### Returns

```python
float
```

Metric score.

---

## Example Workflow

```python
from genai_core.evaluation.factory import (
    EvaluatorFactory
)

predictions = [
    "Paris is the capital of France"
]

references = [
    "The capital of France is Paris"
]

evaluator = (
    EvaluatorFactory.create(
        "qa"
    )
)

results = evaluator.evaluate(
    predictions,
    references
)

print(results)
```

---
