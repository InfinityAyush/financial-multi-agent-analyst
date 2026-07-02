# Financial Multi-Agent Analyst
Live working demo - https://financial-multi-agent-analyst.vercel.app/

An end-to-end **Agentic AI application** that performs comprehensive investment analysis using multiple specialized AI agents, Retrieval-Augmented Generation (RAG), real-time financial data, and SEC filing analysis.

The system analyzes a company from multiple perspectives and generates a final investment recommendation by simulating a debate between bullish and bearish analysts.

---

# Features

* Multi-Agent Architecture using LangGraph
* SEC Filing Analysis using RAG
* Real-time Stock Market Data
* Financial News Analysis
* Bull vs Bear Investment Debate
* Final Portfolio Recommendation
* FastAPI Backend
* React Frontend
* Gemini + Groq LLM Failover
* ChromaDB Vector Database
* Semantic Search over SEC Filings

---

# Demo Workflow

```text
User Query
     │
     ▼
Planner Agent
     │
     ▼
┌──────────────────────────────────────┐
│                                      │
▼                                      ▼
Market Data Agent              News Agent
│                                      │
└──────────────┬───────────────────────┘
               │
               ▼
      SEC Filing RAG Agent
               │
               ▼
      Bull Analyst Agent
               │
               ▼
      Bear Analyst Agent
               │
               ▼
      Judge Agent
               │
               ▼
Final Investment Recommendation
```

---

# System Architecture

```text
Frontend (React + Vite)
            │
            ▼
Backend API (FastAPI)
            │
            ▼
LangGraph Workflow Engine
            │
            ▼
+----------------------------+
| Specialized AI Agents      |
+----------------------------+
| Planner Agent             |
| Market Data Agent         |
| News Agent                |
| SEC Filing RAG Agent      |
| Bull Analyst Agent        |
| Bear Analyst Agent        |
| Judge Agent               |
+----------------------------+
            │
            ▼
LLM Providers
(Gemini / Groq)
```

---

# Agents

## 1. Planner Agent

Responsible for understanding the user query.

Example:

```text
Analyze NVIDIA for long-term investment
```

Output:

```json
{
    "company": "NVIDIA",
    "investment_horizon": "long-term",
    "tasks": [
        "market_data",
        "news_analysis",
        "sec_analysis",
        "risk_assessment"
    ]
}
```

---

## 2. Market Data Agent

Fetches real-time stock information using Yahoo Finance.

Information collected:

* Current Price
* Market Cap
* PE Ratio
* Sector
* Industry
* 52 Week High
* 52 Week Low

---

## 3. News Agent

Collects recent financial news related to the company.

Provides:

* News Title
* Publisher
* News URL

---

## 4. SEC Filing RAG Agent

Analyzes SEC filings using Retrieval-Augmented Generation.

Pipeline:

```text
PDF Filing
    │
    ▼
PyPDF Loader
    │
    ▼
Text Chunking
    │
    ▼
Embeddings
    │
    ▼
ChromaDB
    │
    ▼
Semantic Retrieval
    │
    ▼
LLM Analysis
```

The RAG agent extracts:

* Business Overview
* Key Risks
* Growth Opportunities
* Long-Term Outlook

---

## 5. Bull Analyst Agent

Acts as a bullish portfolio manager.

Focuses on:

* Growth potential
* Competitive advantages
* Market leadership
* Financial strength

---

## 6. Bear Analyst Agent

Acts as a bearish portfolio manager.

Focuses on:

* Risks
* Competition
* Valuation concerns
* Regulatory issues

---

## 7. Judge Agent

Evaluates both bull and bear arguments and generates:

* BUY / HOLD / AVOID recommendation
* Confidence Score
* Key Strengths
* Key Risks
* Final Verdict

---

# Tech Stack

## Backend

* FastAPI
* LangGraph
* LangChain
* ChromaDB
* Pydantic
* Python

## Frontend

* React
* Vite
* Tailwind CSS
* Axios

## LLMs

* Gemini
* Groq

## Data Sources

* Yahoo Finance
* SEC Filings

## Vector Database

* ChromaDB

---

# Project Structure

```text
financial-multi-agent-analysis/

├── backend/
│
│   ├── agents/
│   │   ├── planner_agent.py
│   │   ├── market_data_agent.py
│   │   ├── news_agent.py
│   │   ├── sec_rag_agent.py
│   │   ├── bull_agent.py
│   │   ├── bear_agent.py
│   │   └── judge_agent.py
│   │
│   ├── api/
│   │   └── routes.py
│   │
│   ├── config/
│   │   ├── llm.py
│   │   └── llm_router.py
│   │
│   ├── rag/
│   │   ├── ingest.py
│   │   ├── retriever.py
│   │   └── vector_store.py
│   │
│   ├── workflows/
│   │   ├── state.py
│   │   ├── nodes.py
│   │   └── stock_workflow.py
│   │
│   ├── models/
│   │   └── schemas.py
│   │
│   └── main.py
│
├── frontend/
│   ├── src/
│   ├── package.json
│   └── vite.config.js
│
├── data/
│   └── sec_filings/
│
├── .env
├── pyproject.toml
└── README.md
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/<your-username>/financial-multi-agent-analysis.git

cd financial-multi-agent-analysis
```

---

# Backend Setup

Install dependencies:

```bash
uv sync
```

Create `.env`:

```env
GOOGLE_API_KEY=your_google_api_key
GROQ_API_KEY=your_groq_api_key
```

Run backend:

```bash
uv run uvicorn backend.main:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

---

# Frontend Setup

Move to frontend:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Run frontend:

```bash
npm run dev
```

Frontend URL:

```text
http://localhost:5173
```

---

# SEC Filing RAG Setup

Place SEC filings inside:

```text
data/sec_filings/
```

Example:

```text
data/sec_filings/nvidia_10k.pdf
```

Run ingestion:

```bash
uv run test.py
```

This will:

1. Load PDF
2. Split document into chunks
3. Create embeddings
4. Store embeddings in ChromaDB

---

# API Endpoints

## Analyze Company

### Request

```http
POST /full-analysis
```

Body:

```json
{
    "query": "Analyze NVIDIA for long-term investment"
}
```

### Response

```json
{
    "company": "NVIDIA",
    "market_data": {},
    "news_data": {},
    "sec_analysis": "...",
    "bull_case": "...",
    "bear_case": "...",
    "final_recommendation": {
        "recommendation": "HOLD",
        "confidence_score": 75
    }
}
```

---

## Compare Companies

### Request

```http
POST /compare
```

Body:

```json
{
    "company_1": "NVIDIA",
    "company_2": "AMD"
}
```

---

# LLM Failover

The application automatically switches providers if one becomes unavailable.

Priority:

```text
Gemini
   ↓
Groq
```

This improves reliability during:

* Quota exhaustion
* Rate limits
* API outages

---

# Future Improvements

* Parallel Agent Execution
* Memory Integration
* Real-time Streaming Responses
* Docker Deployment
* Cloud Deployment
* Company Comparison Dashboard
* Historical Performance Tracking
* Portfolio Optimization Agent

---

# Sample Query

```text
Analyze NVIDIA for long-term investment
```

```text
Compare NVIDIA and AMD
```

---

# Author

Ayush Pawar

Graduate in Artificial Intelligence and Data Science, IIIT Kurnool
