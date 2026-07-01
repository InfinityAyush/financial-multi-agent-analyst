from typing import TypedDict


class StockAnalysisState(TypedDict):

    user_query: str

    company: str
    investment_horizon: str
    tasks: list[str]

    market_data: dict
    news_data: dict
    sec_analysis: str

    bull_case: str
    bear_case: str

    final_recommendation: dict