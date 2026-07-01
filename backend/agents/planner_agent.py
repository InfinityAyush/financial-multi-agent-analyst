import json
from backend.config.llm_router import get_llm

llm = get_llm()

SYSTEM_PROMPT = """
You are a financial planning agent.

Your task is to analyze the user's request and return:

1. Company name
2. Investment horizon
3. Required analysis tasks

Return ONLY valid JSON.

Example:

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
"""

def planner_agent(user_query: str):

    prompt = f"""
    User Query:
    {user_query}
    """

    response = llm.invoke(
        SYSTEM_PROMPT + prompt
    )

    print("\n========== RAW GEMINI RESPONSE ==========")
    print(repr(response.content))
    print("=========================================\n")

    try:
        # Remove markdown code fences
        cleaned_response = response.content.strip()
        cleaned_response = cleaned_response.replace("```json", "")
        cleaned_response = cleaned_response.replace("```", "")
        cleaned_response = cleaned_response.strip()

        result = json.loads(cleaned_response)

    except Exception as e:
        print("JSON Parsing Error:", e)

        result = {
            "company": "Unknown",
            "investment_horizon": "Unknown",
            "tasks": []
        }

    return result