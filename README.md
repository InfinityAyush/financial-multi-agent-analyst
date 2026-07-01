# Financial Multi-Agent Analyst

An Agentic AI system that performs investment analysis using multiple specialized AI agents, RAG, and real-time financial data.

## Features

- Multi-Agent Architecture using LangGraph
- SEC Filing Analysis using RAG
- Real-time Market Data via Yahoo Finance
- Financial News Analysis
- Bull vs Bear Investment Debate
- Final Portfolio Recommendation
- FastAPI Backend
- React Frontend
- Gemini + Groq LLM Failover

## Architecture

User Query
↓
Planner Agent
↓
Market Agent | News Agent | SEC RAG Agent
↓
Bull Agent | Bear Agent
↓
Judge Agent
↓
Final Recommendation

## Tech Stack

- FastAPI
- React
- LangGraph
- ChromaDB
- HuggingFace Embeddings
- Gemini
- Groq
- Yahoo Finance

## Running Locally

### Backend

```bash
uv sync
uv run uvicorn backend.main:app --reload