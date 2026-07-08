# AI Incident Resolver

AI-powered incident investigation platform using:

- Gemini LLM
- LangGraph
- ChromaDB
- FastAPI
- Docker
- Kubernetes

## Features

- Log Analysis
- Root Cause Analysis
- Knowledge Retrieval
- AI Resolution Suggestions
- Infrastructure Diagnostics

## Architecture

Logs
↓
RAG Engine
↓
LangGraph Agent
↓
Gemini
↓
Resolution

## Run

```bash
python src/api.py
```

## Docker

```bash
docker build -t incident-ai .
docker run -p 8000:8000 incident-ai
```