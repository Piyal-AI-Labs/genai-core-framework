# Experiment Tracking Module

A lightweight experiment tracking system for recording and managing research experiments.

This module provides a simple way to store experiment configurations, metrics, metadata, and results in a structured and reproducible format. The goal is to make research experiments easier to reproduce, compare, and analyze across different projects.

---

## Features

### Experiment Tracking

* Track experiment parameters
* Track evaluation metrics
* Store experiment metadata
* Automatic experiment IDs
* Timestamped experiment records

### Experiment Storage

* JSON-based storage
* Human-readable records
* Easy integration with Git
* No external services required

---

## Why Use This Module?

Research experiments often involve testing different:

* Models
* Prompts
* Embedding methods
* Retrieval strategies
* Hyperparameters

Without proper tracking, it becomes difficult to remember:

* What was tested
* Which configuration was used
* Which experiment produced the best results

This module automatically records experiment details in a structured format.

Example:

```python
tracker = ExperimentTracker(
    experiment_name="rag_chunking"
)

tracker.log_param(
    "chunk_size",
    512
)

tracker.log_metric(
    "faithfulness",
    0.91
)

tracker.save()
```

---

## Module Structure

```text
experiments/
│
├── schemas.py
├── storage.py
├── tracker.py
├── utils.py
└── __init__.py
```

### schemas.py

Defines experiment data models and validation schemas.

### storage.py

Handles saving and loading experiment records.

### tracker.py

Provides the main experiment tracking interface.

### utils.py

Utility functions for listing and loading experiments.

---

## Installation

Install the required dependency:

```bash
pip install pydantic
```

No database or external tracking server is required.

---

## Quick Start

### Create an Experiment

```python
from genai_core.experiments.tracker import (
    ExperimentTracker
)

tracker = ExperimentTracker(
    experiment_name="embedding_comparison"
)
```

---

### Log Parameters

```python
tracker.log_param(
    "embedding_model",
    "bge-small"
)

tracker.log_param(
    "chunk_size",
    512
)
```

Parameters describe the experiment configuration.

---

### Log Metrics

```python
tracker.log_metric(
    "accuracy",
    0.84
)

tracker.log_metric(
    "faithfulness",
    0.91
)
```

Metrics record experiment performance.

---

### Log Metadata

```python
tracker.log_metadata(
    "dataset",
    "hotpotqa"
)

tracker.log_metadata(
    "research_area",
    "rag"
)
```

Metadata stores additional information about the experiment.

---

### Save Experiment

```python
tracker.save()
```

This creates a JSON record inside the experiments directory.

---

## Example Output

The experiment will be saved as a JSON file:

```json
{
    "experiment_id": "a1b2c3d4",
    "experiment_name": "rag_chunking",
    "created_at": "2026-06-03T10:00:00",
    "parameters": {
        "embedding_model": "bge-small",
        "chunk_size": 512
    },
    "metrics": {
        "accuracy": 0.84,
        "faithfulness": 0.91
    },
    "metadata": {
        "dataset": "hotpotqa"
    }
}
```

---

## Experiment Storage Structure

```text
outputs/
│
├── experiments/
│   ├── experiment_001.json
│   ├── experiment_002.json
│   └── experiment_003.json
│
├── reports/
│
└── figures/
```

This structure keeps experiment results organized and easy to analyze later.

---
