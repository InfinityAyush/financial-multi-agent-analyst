from pydantic import BaseModel
from typing import List


class QueryRequest(BaseModel):
    query: str


class PlannerResponse(BaseModel):
    company: str
    investment_horizon: str
    tasks: List[str]


class FinalRecommendation(BaseModel):

    recommendation: str

    confidence_score: int

    key_strengths: List[str]

    key_risks: List[str]

    verdict: str

class FullAnalysisResponse(BaseModel):

    company: str

    market_data: dict

    news_data: dict

    sec_analysis: str

    bull_case: str

    bear_case: str

    final_recommendation: FinalRecommendation


