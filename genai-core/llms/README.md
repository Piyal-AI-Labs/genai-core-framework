# LLM Module (v1.0)

A simple and unified interface for working with different Large Language Model (LLM) providers.

Instead of writing separate code for OpenAI, Ollama, or other providers, this module gives you a single interface that works across all supported models. This makes it easier to build experiments, benchmarks, and AI applications without changing your core code.

---

## Features

### Supported Providers

#### OpenAI

#### Ollama


---

## Why Use This Module?

Without this module, you need provider-specific code. For example:

```python
from openai import OpenAI

client = OpenAI()
response = client.responses.create(...)
```


With the LLM module, you use the same interface everywhere:

```python
llm = LLMFactory.create(
    provider="openai",
    model="gpt-4o"
)

response = llm.generate(
    "Explain Retrieval-Augmented Generation."
)
```

Switching providers only requires changing the configuration:

```python
provider="ollama"
model="llama3"
```

No other code changes are needed.

---

## Module Structure

```text
llms/
│
├── base.py
├── schemas.py
├── openai_llm.py
├── ollama_llm.py
└── factory.py
```

### base.py

Defines the common interface that every LLM provider must implement.

### schemas.py

Contains configuration and validation schemas.

### openai_llm.py

OpenAI implementation.

### ollama_llm.py

Ollama implementation.

### factory.py

Creates the appropriate LLM instance based on the selected provider.

---

## Installation

Install the required dependencies:

```bash
pip install openai
pip install ollama
pip install pydantic
```

---

## Quick Start

### OpenAI Example

```python
from genai_core.llms.factory import LLMFactory

llm = LLMFactory.create(
    provider="openai",
    model="gpt-4o",
    api_key="YOUR_API_KEY"
)

response = llm.generate(
    "What is Retrieval-Augmented Generation?"
)

print(response)
```

The same workflow can run with any supported provider by changing only the provider configuration.

---