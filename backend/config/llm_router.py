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

    try:
        llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            google_api_key=os.getenv("GOOGLE_API_KEY"),
            temperature=0,
        )

        llm.invoke("hello")

        print("Using Gemini")

        _cached_llm = llm
        return llm

    except Exception as e:
        print(f"Gemini unavailable: {e}")

    try:
        llm = ChatGroq(
            model="llama-3.3-70b-versatile",
            api_key=os.getenv("GROQ_API_KEY"),
            temperature=0,
        )

        print("Using Groq")

        _cached_llm = llm
        return llm

    except Exception as e:
        print(f"Groq unavailable: {e}")
        raise Exception("No LLM provider available")