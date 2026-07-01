from backend.config.llm_router import get_llm

llm = get_llm()


def bull_agent(
    market_data: dict,
    news_data: dict,
    sec_analysis: str
):

    prompt = f"""
You are an optimistic Wall Street analyst.

Your job is to build the strongest possible investment case.

Market Data:
{market_data}

News:
{news_data}

SEC Analysis:
{sec_analysis}

Create a bullish investment thesis.

Include:

1. Strengths
2. Growth drivers
3. Competitive advantages
4. Reasons investors should buy

Be persuasive.
"""

    response = llm.invoke(prompt)

    return response.content