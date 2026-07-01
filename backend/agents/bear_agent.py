from backend.config.llm_router import get_llm

llm = get_llm()


def bear_agent(
    market_data: dict,
    news_data: dict,
    sec_analysis: str
):

    prompt = f"""
You are a skeptical hedge fund analyst.

Your job is to identify every possible risk.

Market Data:
{market_data}

News:
{news_data}

SEC Analysis:
{sec_analysis}

Create a bearish investment thesis.

Include:

1. Risks
2. Weaknesses
3. Regulatory concerns
4. Reasons investors should avoid the stock

Be critical.
"""

    response = llm.invoke(prompt)

    return response.content