from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
from backend.api.routes import router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",  # React Vite frontend
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Docker and Render use this to know if your app is alive

 
@app.get("/health")
async def health_check():
    """
    Health check endpoint.
    Docker healthcheck + Render deployment monitor + uptime tools all call this.
    Must return 200 with a fast response — no LLM calls here.
    """
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "service": "financial-multi-agent-analyst",
        "version": "1.0.0"
    }



app.include_router(router)