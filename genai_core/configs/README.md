# Configuration Module (v1.0)

A simple configuration management system for AI experiments and research projects.

This module provides a centralized way to manage application settings, model configurations, embedding configurations, and experiment parameters using YAML files.

The goal is to improve reproducibility, maintainability, and experiment management by separating configuration from code.

---

## Features

### Configuration Management

* YAML-based configuration files
* Configuration validation using Pydantic
* Type-safe configuration objects
* Centralized experiment settings
* Easy integration across modules

### Reproducible Research

* Store experiment settings in version-controlled files
* Separate configuration from implementation
* Simplify experiment comparisons
* Reduce hardcoded values

---

## Why Use This Module?

Without a configuration system, experiment settings are often hardcoded directly into Python files:

```python
llm = LLMFactory.create(
    provider="openai",
    model="gpt-4o"
)

embedding_model = (
    "BAAI/bge-small-en-v1.5"
)

chunk_size = 512
```

This approach makes experiments difficult to reproduce and maintain.

With the Configuration Module:

```python
config = ConfigLoader.load(
    "configs/rag.yaml"
)

llm = LLMFactory.create(
    provider=config.llm.provider,
    model=config.llm.model
)
```

All experiment settings are managed in a single configuration file.

---

## Module Structure

```text
configs/
│
├── loader.py
├── schemas.py
├── exceptions.py
└── __init__.py
```

### loader.py

Loads and validates YAML configuration files.

### schemas.py

Contains configuration models and validation schemas.

### exceptions.py

Defines custom configuration exceptions.

---

## Installation

Install the required dependencies:

```bash
pip install pydantic
pip install pyyaml
```

---

## Quick Start

### Create a Configuration File

Create a YAML configuration file:

```yaml
llm:
  provider: openai
  model: gpt-4o
  temperature: 0.2
  max_tokens: 1000

embeddings:
  provider: sentence_transformer
  model: BAAI/bge-small-en-v1.5

experiment:
  name: rag_chunking_experiment
  output_dir: outputs
```

---

### Load Configuration

```python
from genai_core.configs.loader import (
    ConfigLoader
)

config = ConfigLoader.load(
    "configs/rag.yaml"
)
```

---

### Access Configuration Values

```python
print(
    config.llm.provider
)

print(
    config.llm.model
)

print(
    config.embeddings.model
)

print(
    config.experiment.name
)
```

---

## Configuration Schema

### LLM Configuration

```yaml
llm:
  provider: openai
  model: gpt-4o
  temperature: 0.7
  max_tokens: 1000
```

| Field       | Type  | Description            |
| ----------- | ----- | ---------------------- |
| provider    | str   | LLM provider name      |
| model       | str   | Model identifier       |
| temperature | float | Generation temperature |
| max_tokens  | int   | Maximum output tokens  |

---

### Embedding Configuration

```yaml
embeddings:
  provider: sentence_transformer
  model: BAAI/bge-small-en-v1.5
```

| Field    | Type | Description        |
| -------- | ---- | ------------------ |
| provider | str  | Embedding provider |
| model    | str  | Embedding model    |

---

### Experiment Configuration

```yaml
experiment:
  name: rag_chunking_experiment
  output_dir: outputs
```

| Field      | Type | Description      |
| ---------- | ---- | ---------------- |
| name       | str  | Experiment name  |
| output_dir | str  | Output directory |

---

## Example Workflow

### Load Configuration

```python
config = ConfigLoader.load(
    "configs/rag.yaml"
)
```

### Initialize LLM

```python
llm = LLMFactory.create(
    provider=config.llm.provider,
    model=config.llm.model,
    api_key=api_key
)
```

### Initialize Embeddings

```python
embedding = (
    EmbeddingFactory.create(
        provider=config.embeddings.provider,
        model=config.embeddings.model
    )
)
```

### Initialize Experiment Tracking

```python
tracker = ExperimentTracker(
    config.experiment.name
)
```

All modules now use a shared configuration source.

---

## Recommended Structure for Future Projects

```text
configs/
│
├── rag/
│   ├── baseline.yaml
│   ├── chunk_256.yaml
│   └── chunk_512.yaml
│
├── evaluation/
│   ├── bertscore.yaml
│   └── rouge.yaml
│
├── adaptation/
│   ├── lora.yaml
│   └── qlora.yaml
│
└── trustworthy/
    └── hallucination.yaml
```

This structure keeps experiment configurations organized and easy to manage.
