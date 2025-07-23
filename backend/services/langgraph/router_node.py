from backend.services.shared.github_llm import GitHubChatLLM
from langchain.schema import HumanMessage
import logging
from backend.services.langgraph.state_model import AgentState

# Prompt to classify query type
def generate_routing_prompt(query: str) -> str:
    return f"""
        You are a router for ZeeAgentX — a GenAI assistant that has two response systems:

        1. **agent** — Use for general queries like:
        - Greetings or casual messages ("Hi", "How are you?")
        - Real-time tools (time, weather, currency, YouTube, etc.)
        - General knowledge, reasoning, or web search

        2. **rag** — Use only if the query:
        - Relates to uploaded documents
        - Requires deep domain-specific or niche knowledge

        Rules:
        - Reply with only one word: `agent` or `rag`
        - If unsure, default to `agent`
        - Do NOT explain, apologize, or output anything else

        User query:
        \"{query}\"
        """


# Load your GitHub-hosted model (via your custom wrapper)
llm = GitHubChatLLM(model="openai/gpt-4.1", temperature=0.3)

# LangGraph router node
def router_node(state: AgentState) -> str:
    prompt = generate_routing_prompt(state.query)
    message = HumanMessage(content=prompt)

    default = "agent" # Default to agent if LLM fails or gives unexpected output
    try:
        decision = llm.invoke({"messages": [message]}).content.strip().lower()
        if decision not in {"agent", "rag"}:
            decision = default
    except Exception:
        logging.exception("Router node LLM failure")
        decision = default

    state.route = decision
    return state

