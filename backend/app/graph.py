from typing import TypedDict
from langgraph.graph import StateGraph, END

from .tools import (
    log_interaction,
    edit_interaction,
    search_hcp,
    interaction_history,
    followup_recommendation,
)


class CRMState(TypedDict):
    action: str
    data: dict
    result: dict


def execute_tool(state: CRMState):

    action = state["action"]
    data = state["data"]

    if action == "log":
        result = log_interaction.invoke({"data": data})

    elif action == "edit":
        result = edit_interaction.invoke({
            "interaction_id": data.get("id", 0),
            "updated_data": data
        })

    elif action == "search":
        result = search_hcp.invoke({
            "name": data.get("hcp_name", "")
        })

    elif action == "history":
        result = interaction_history.invoke({
            "hcp_name": data.get("hcp_name", "")
        })

    elif action == "followup":
        result = followup_recommendation.invoke({
            "summary": data.get("summary", "")
        })

    else:
        result = {
            "status": "error",
            "message": "Unknown action"
        }

    return {"result": result}


builder = StateGraph(CRMState)

builder.add_node("execute_tool", execute_tool)

builder.set_entry_point("execute_tool")

builder.add_edge("execute_tool", END)

graph = builder.compile()