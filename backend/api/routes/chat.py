from fastapi import APIRouter
from backend.api.schemas.response_models import QueryInput, QueryResponse
from backend.utils.db_utils import insert_application_logs, get_chat_history
from backend.services.langgraph.flow_builder import build_zeeagentx_flow
from backend.services.langgraph.state_model import AgentState
import uuid, logging

router = APIRouter()

@router.post("/chat", response_model=QueryResponse)
def chat(query_input: QueryInput):
    session_id = query_input.session_id or str(uuid.uuid4())
    logging.info(f"Session ID: {session_id}, User Query: {query_input.question}, Model: {query_input.model.value}")

    # Fetch chat history from DB 
    chat_history = get_chat_history(session_id)

    # Build and run LangGraph flow
    workflow = build_zeeagentx_flow()
    agent_state = AgentState(query=query_input.question, context={"chat_history": chat_history})
    result = workflow.invoke(agent_state)

    # Access response from the result dict
    insert_application_logs(session_id, query_input.question, result["response"], query_input.model.value)

    return QueryResponse(
        answer=result["response"],
        session_id=session_id,
        model=query_input.model
    )