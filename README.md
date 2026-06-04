# GenAI Core Framework

A lightweight framework for building, evaluating, and experimenting with Generative AI systems.

The framework provides reusable components that can be shared across multiple research projects, reducing duplicated code and improving experiment reproducibility.

This repository serves as the foundation for all projects within **Piyal-AI-Labs**.

---

## Purpose

The goal of this framework is to provide common building blocks for:

* LLM applications
* RAG systems
* Agentic AI systems
* Evaluation pipelines
* Fine-tuning experiments
* Multimodal AI research

Rather than rewriting the same code for every project, researchers can reuse standardized components from a single framework.

---

## Core Modules

### LLM Module

Unified interface for working with different language models.

Supported providers:

* OpenAI
* Ollama
* Future providers

---

### Embedding Module

Unified interface for generating embeddings.

Supported providers:

* OpenAI Embeddings
* Sentence Transformers

---

### Metrics Module

Evaluation metrics for benchmarking AI systems.

Current metrics:

* Accuracy
* BLEU
* ROUGE
* BERTScore

---

### Experiment Tracking Module

Track and store:

* Parameters
* Metrics
* Metadata
* Experiment results

---

### Configuration Module

Centralized YAML-based configuration management.

Benefits:

* Reproducibility
* Easy experimentation
* Cleaner code

---

### Prompt Templates Module

Reusable prompt management using templates.

Features:

* Prompt versioning
* Dynamic rendering
* Experiment-friendly workflows

---

## Repository Structure

```text
genai-core-framework/
│
├── genai-core
│   ├── llms/
│   ├── embeddings/
│   ├── evaluation/
│   ├── experiments/
│   ├── configs/
│   ├── prompts/
│
└── README.md
```

---

## Design Principles

* Simple and modular
* Research-focused
* Reusable components
* Reproducible experiments
* Framework-agnostic
* Easy to extend

---

## Future Roadmap

Planned additions:

* RAG Evaluation Metrics
* LLM-as-a-Judge Evaluation
* Reranker Support
* Retrieval Utilities
* Caching
* Observability
* Multimodal Support

---

## Author

**Piyal Banik**

Applied Generative AI Research

**Piyal-AI-Labs**
