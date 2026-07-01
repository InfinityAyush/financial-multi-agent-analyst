import os
from pathlib import Path
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq

env_path = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(dotenv_path=env_path)

_cached_llm = None


def get_llm():
    global _cached_llm

    if _cached_llm is not None:
        return _cached_llm

    # ── Try Groq FIRST (14,400 req/day free vs Gemini's 20/day) ──
    try:
        llm = ChatGroq(
            model="llama-3.3-70b-versatile",
            api_key=os.getenv("GROQ_API_KEY"),
            temperature=0,
        )
        llm.invoke("hi")  # verify key works
        print("✅ Using Groq (Llama 3.3 70B)")
        _cached_llm = llm
        return llm

    except Exception as e:
        print(f"⚠️ Groq unavailable: {e}")

    # ── Fallback to Gemini 1.5 Flash (1,500 req/day free) ──
    try:
        llm = ChatGoogleGenerativeAI(
            model="gemini-1.5-flash",   # 1,500/day vs 2.5-flash's 20/day
            google_api_key=os.getenv("GOOGLE_API_KEY"),
            temperature=0,
        )
        llm.invoke("hi")  # verify key works
        print("✅ Using Gemini 1.5 Flash")
        _cached_llm = llm
        return llm

    except Exception as e:
        print(f"⚠️ Gemini unavailable: {e}")

    raise Exception("❌ No LLM available. Check GROQ_API_KEY and GOOGLE_API_KEY")