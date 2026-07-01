from backend.agents.planner_agent import planner_agent
from backend.agents.market_data_agent import market_data_agent
from backend.agents.news_agent import news_agent
from backend.agents.sec_rag_agent import sec_rag_agent

from backend.agents.bull_agent import bull_agent
from backend.agents.bear_agent import bear_agent
from backend.agents.judge_agent import judge_agent


# sec node
def sec_node(state):

    result = sec_rag_agent(
        state["user_query"]
    )

    return {
        "sec_analysis": result
    }

# Bull Node
def bull_node(state):

    result = bull_agent(
        state["market_data"],
        state["news_data"],
        state["sec_analysis"]
    )

    return {
        "bull_case": result
    }

# Bear Node
def bear_node(state):

    result = bear_agent(
        state["market_data"],
        state["news_data"],
        state["sec_analysis"]
    )

    return {
        "bear_case": result
    }

# Judge Node
def judge_node(state):

    result = judge_agent(
        state["bull_case"],
        state["bear_case"]
    )

    return {
        "final_recommendation": result
    }

# Planner Node
def planner_node(state):

    result = planner_agent(state["user_query"])

    return {
        "company": result["company"],
        "investment_horizon": result["investment_horizon"],
        "tasks": result["tasks"]
    }

# Market Node
def market_node(state):

    result = market_data_agent(
        state["company"]
    )

    return {
        "market_data": result
    }

# News Node
def news_node(state):

    result = news_agent(
        state["company"]
    )

    return {
        "news_data": result
    }