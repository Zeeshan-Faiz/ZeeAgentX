from backend.services.langgraph.state_model import AgentState
from backend.services.rag_pipeline.chains.rag_chain_builder import get_rag_chain

# Preload RAG chain
rag_chain = get_rag_chain(model="openai/gpt-4o-mini")

def run_rag_chain(state: AgentState) -> AgentState:
    """
    This is the main LangGraph node that handles RAG queries.
    It assumes that the query is already present in state.query.
    It will return a modified AgentState with .response field populated.
    """
    try:
        inputs = {
            "input": state.query,
            "chat_history": [],  # You can use state.context["chat_history"] if available
        }
        result = rag_chain.invoke(inputs)
        state.response = result
    except Exception as e:
        state.response = f"RAG system encountered an error: {str(e)}"
    
    return state
