from backend.services.langgraph.state_model import AgentState
from backend.services.agent_workflow.chains.agent_chain_builder import get_agent_executor
from langchain.memory import ConversationBufferMemory
from backend.api.schemas.chat_models import ModelName
import logging

# Setup logger
logger = logging.getLogger(__name__)

def run_agent_workflow(state: AgentState) -> AgentState:
    try:
        query = state.query
        memory = ConversationBufferMemory(return_messages=True)

        # Use the same model as rest of system
        agent_executor = get_agent_executor(model_enum=ModelName.GPT_4_1, memory=memory)

        result = agent_executor.invoke({"input": query})
        state.response = result if isinstance(result, str) else result.get("output", str(result))

    except Exception as e:
        logger.exception("Agent execution failed")
        state.response = f"Agent workflow encountered an error: {str(e)}"

    return state
