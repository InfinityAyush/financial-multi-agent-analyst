from fastapi import APIRouter

from backend.models.schemas import (
    QueryRequest,
    PlannerResponse
)

from backend.agents.planner_agent import planner_agent
from backend.agents.market_data_agent import market_data_agent

from backend.workflows.stock_workflow import graph

from backend.models.schemas import (
    QueryRequest,
    FullAnalysisResponse
)

from pydantic import BaseModel


class CompareRequest(BaseModel):
    company_1: str
    company_2: str

router = APIRouter()


@router.post("/analyze",
             response_model=PlannerResponse)
def analyze_stock(request: QueryRequest):

    result = planner_agent(request.query)

    return result


@router.post("/market-data")
def get_market_data(request: QueryRequest):

    plan = planner_agent(request.query)

    market_data = market_data_agent(
        plan["company"]
    )
    return market_data

@router.post(
    "/full-analysis",
    response_model=FullAnalysisResponse
)
def full_analysis(request: QueryRequest):
    result = graph.invoke(
        {
            "user_query": request.query
        }
    )

    return {
        "company":
            result["company"],

        "market_data":
            result["market_data"],

        "news_data":
            result["news_data"],

        "sec_analysis":
            result["sec_analysis"],

        "bull_case":
            result["bull_case"],

        "bear_case":
            result["bear_case"],

        "final_recommendation":
            result["final_recommendation"]
    }

@router.post("/compare")
def compare_companies(
    request: CompareRequest
):

    company1 = graph.invoke(
        {
            "user_query":
            f"Analyze {request.company_1} for long-term investment"
        }
    )

    company2 = graph.invoke(
        {
            "user_query":
            f"Analyze {request.company_2} for long-term investment"
        }
    )

    return {
        request.company_1:
            company1["final_recommendation"],

        request.company_2:
            company2["final_recommendation"]
    }