from typing import TypedDict

from langgraph.graph import StateGraph, END

import ollama


class AgentState(TypedDict):

    analytics: dict
    insights: list
    anomalies: list
    spending_trend: str

    recommendation: str


def generate_budget_plan(state: AgentState):

    prompt = f"""
You are an autonomous AI financial planning agent.

Analyze the user's financial state and generate:
- budgeting strategy
- spending reduction ideas
- savings optimization
- anomaly observations
- practical action plan

Financial Analytics:
{state['analytics']}

Insights:
{state['insights']}

Spending Trend:
{state['spending_trend']}

Anomalies:
{state['anomalies']}

Generate a professional financial action plan.
"""

    response = ollama.chat(
        model="phi3:mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    state["recommendation"] = (
        response["message"]["content"]
    )

    return state


# Build graph
graph = StateGraph(AgentState)

graph.add_node(
    "budget_planner",
    generate_budget_plan
)

graph.set_entry_point("budget_planner")

graph.add_edge(
    "budget_planner",
    END
)

budget_agent = graph.compile()