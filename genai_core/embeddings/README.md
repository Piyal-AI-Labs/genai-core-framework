# Embedding Module (v1.0)

A simple and unified interface for generating vector embeddings using different embedding providers.

Instead of writing separate code for OpenAI embeddings, Sentence Transformers, or other embedding models, this module provides a common interface that works across all supported providers. This makes it easier to build retrieval systems, semantic search applications, RAG pipelines, and benchmarking experiments.

---

## Supported Providers

#### OpenAI

#### Sentence Transformers

---

## Why Use This Module?

Without this module, you need provider-specific code. For example:

```python
from openai import OpenAI

client = OpenAI()

embedding = client.embeddings.create(
    model="text-embedding-3-small",
    input="What is RAG?"
)
```


With the Embedding module, you use the same interface everywhere:

```python
embedding = EmbeddingFactory.create(
    provider="openai",
    model="text-embedding-3-small"
)

vector = embedding.embed_text(
    "What is Retrieval-Augmented Generation?"
)
```

Switching providers only requires changing the configuration:

```python
provider="sentence_transformer"
model="BAAI/bge-small-en-v1.5"
```

No other code changes are needed.

---

## Module Structure

```text
embeddings/
│
├── base.py
├── schemas.py
├── openai_embedding.py
├── sentence_embedding.py
└── factory.py
```

### base.py

Defines the common interface that every embedding provider must implement.

### schemas.py

Contains configuration and validation schemas.

### openai_embedding.py

OpenAI embedding implementation.

### sentence_embedding.py

Sentence Transformer implementation.

### factory.py

Creates the appropriate embedding instance based on the selected provider.

---

## Installation

Install the required dependencies:

```bash
pip install openai
pip install sentence-transformers
pip install pydantic
```

---

## Quick Start

### OpenAI Example

```python
from genai_core.embeddings.factory import (
    EmbeddingFactory
)

embedding = EmbeddingFactory.create(
    provider="openai",
    model="text-embedding-3-small",
    api_key="YOUR_API_KEY"
)

vector = embedding.embed_text(
    "What is Retrieval-Augmented Generation?"
)

print(len(vector))
```

---

## Example Workflow

```python
from genai_core.embeddings.factory import (
    EmbeddingFactory
)

embedding = EmbeddingFactory.create(
    provider="sentence_transformer",
    model="BAAI/bge-small-en-v1.5"
)

documents = [
    "RAG improves factuality.",
    "Fine-tuning adapts models.",
    "Agents use tools."
]

vectors = embedding.embed_documents(
    documents
)

print(
    f"Generated {len(vectors)} embeddings"
)
```

The same workflow can run with any supported provider by changing only the provider configuration.

---
