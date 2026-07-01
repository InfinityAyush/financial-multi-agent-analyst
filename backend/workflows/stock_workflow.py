from langgraph.graph import (
    StateGraph,
    START,
    END
)

from backend.workflows.state import StockAnalysisState

from backend.workflows.nodes import *

workflow = StateGraph(
    StockAnalysisState
)
workflow.add_node("planner", planner_node)

workflow.add_node("market", market_node)
workflow.add_node("news", news_node)
workflow.add_node("sec", sec_node)

workflow.add_node("bull", bull_node)
workflow.add_node("bear", bear_node)

workflow.add_node("judge", judge_node)

# Start

workflow.add_edge(START, "planner")

# Parallel execution

workflow.add_edge("planner", "market")
workflow.add_edge("planner", "news")
workflow.add_edge("planner", "sec")

# Bull and Bear need all previous results

workflow.add_edge("market", "bull")
workflow.add_edge("news", "bull")
workflow.add_edge("sec", "bull")

workflow.add_edge("market", "bear")
workflow.add_edge("news", "bear")
workflow.add_edge("sec", "bear")

# Judge waits for both

workflow.add_edge("bull", "judge")
workflow.add_edge("bear", "judge")

workflow.add_edge("judge", END)

graph = workflow.compile()