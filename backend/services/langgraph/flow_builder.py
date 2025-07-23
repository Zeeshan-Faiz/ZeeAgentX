from langgraph.graph import StateGraph, END
from backend.services.langgraph.state_model import AgentState
from backend.services.langgraph.router_node import router_node
from backend.services.rag_pipeline.rag_executor import run_rag_chain
from backend.services.agent_workflow.agent_executor import run_agent_workflow
from backend.services.shared.github_llm import GitHubChatLLM
from langchain.schema import HumanMessage

def get_route_from_state(state: AgentState) -> str:
    return state.route

def build_zeeagentx_flow():
    builder = StateGraph(AgentState)

    # Register all nodes
    builder.add_node("router_node", router_node)
    builder.add_node("rag_node", run_rag_chain)
    builder.add_node("agent_node", run_agent_workflow)

    # Entry point
    builder.set_entry_point("router_node")

    # the correct way to pass conditional edges
    builder.add_conditional_edges(
        "router_node",
        get_route_from_state,
        {
            "agent": "agent_node",
            "rag": "rag_node",
        }
    )

    # End nodes
    builder.add_edge("agent_node", END)
    builder.add_edge("rag_node", END)

    return builder.compile()
