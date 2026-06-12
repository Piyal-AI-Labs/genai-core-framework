# Prompt Templates Module

A simple and reusable prompt management system for Generative AI applications and research experiments.

This module allows prompts to be stored as external template files and rendered dynamically using variables. The goal is to make prompts easier to maintain, version, reuse, and evaluate across different experiments.

Instead of hardcoding prompts directly in Python code, prompts can be managed as reusable templates that support dynamic content injection.

---

## Features

### Prompt Management

* Template-based prompts
* Dynamic variable rendering
* Jinja2-powered templating
* Reusable prompt structures
* Organized prompt storage

---

## Why Use This Module?

Without a prompt management system, prompts are often embedded directly in code:

```python
prompt = f"""
You are a helpful AI assistant.

Context:
{context}

Question:
{question}

Answer:
"""
```

This quickly becomes difficult to manage as projects grow.

With the Prompt Templates Module:

```python
prompt = prompt_manager.render(
    "rag/basic.jinja2",
    context=context,
    question=question
)
```

Prompts remain separate from application logic and can be updated without changing code.

---

## Module Structure

```text
prompts/
│
├── loader.py
├── manager.py
├── schemas.py
├── exceptions.py
│
└── templates/
    │
    ├── rag/
    │   ├── basic.jinja2
    │   └── grounded.jinja2
    │
    ├── evaluation/
    │   └── judge.jinja2
    │
    └── adaptation/
        └── few_shot.jinja2
```

### loader.py

Loads prompt templates from the filesystem.

### manager.py

Renders templates using provided variables.

### schemas.py

Contains prompt-related schemas and models.

### exceptions.py

Defines prompt-related exceptions.

### templates/

Stores all reusable prompt templates.

---

## Installation

Install the required dependency:

```bash
pip install jinja2
pip install pydantic
```

---

## Quick Start

### Create a Prompt Template

Example:

```text
You are a helpful AI assistant.

Context:
{{ context }}

Question:
{{ question }}

Answer:
```

Save as:

```text
templates/rag/basic.jinja2
```

---

### Load and Render a Prompt

```python
from genai_core.prompts.manager import (
    PromptManager
)

prompt_manager = PromptManager(
    template_dir="templates"
)

prompt = prompt_manager.render(
    "rag/basic.jinja2",
    context="Paris is the capital of France.",
    question="What is the capital of France?"
)

print(prompt)
```

---

## Example Workflow

### Render Prompt

```python
prompt = prompt_manager.render(
    "rag/basic.jinja2",
    context=context,
    question=question
)
```

### Generate Response

```python
response = llm.generate(
    prompt
)
```

### Evaluate Response

```python
score = evaluator.evaluate(
    predictions=[response],
    references=[ground_truth]
)
```

The prompt system integrates naturally with the LLM, Evaluation, and Experiment Tracking modules.

---