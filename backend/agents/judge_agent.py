import json

from backend.config.llm import llm


def judge_agent(
        bull_case: str,
        bear_case: str):

    prompt = f"""
You are a senior portfolio manager.

BULL ANALYSIS:
{bull_case}

BEAR ANALYSIS:
{bear_case}

Evaluate both analyses objectively.

Return ONLY valid JSON.

JSON Format:

{{
    "recommendation": "BUY/HOLD/AVOID",
    "confidence_score": 0,
    "key_strengths": [
        "...",
        "...",
        "..."
    ],
    "key_risks": [
        "...",
        "...",
        "..."
    ],
    "verdict": "Final investment summary"
}}

Rules:
1. recommendation must be BUY, HOLD or AVOID.
2. confidence_score must be between 0 and 100.
3. Return ONLY JSON.
4. No markdown.
5. No explanation outside JSON.
"""

    response = llm.invoke(prompt)

    content = response.content.strip()

    # remove markdown if present

    content = content.replace(
        "```json", ""
    ).replace(
        "```", ""
    ).strip()

    print("\nRAW JUDGE RESPONSE:\n")
    print(content)

    return json.loads(content)