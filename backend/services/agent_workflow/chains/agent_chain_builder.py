from langchain import hub
from langchain.agents import create_structured_chat_agent, AgentExecutor
from langchain.memory import ConversationBufferMemory
from langchain_core.messages import SystemMessage

from backend.services.shared.github_llm import GitHubChatLLM
from backend.services.agent_workflow.tool_registry import tools
from backend.api.schemas.chat_models import ModelName  # Enum

# System instruction prompt for agent
initial_message = """You are a smart and helpful AI assistant designed to provide factual, real-time and relevant answers to user queries by using specialized tools when necessary.

        You have access to the following tools:

        1. **Time** — Current time
        2. **Wikipedia** — General knowledge
        3. **Google Search** — News, real-time, uncommon facts
        4. **Stock Checker** — Real-time prices via ticker symbols
        5. **Weather** — City-based or auto-detected
        6. **Currency Converter**
        7. **YouTube Video Search**
        8. **E-commerce Product Search**
        9. **Indian Holiday Lookup**
        10. **Train Live Status**
        11. **PNR Status**
        12. **Flight Status**
        13. **FD Rates**
        14. **Recharge Plan Search**

        Instructions:
        - Use tools when your own knowledge may be outdated or limited.
        - Summarize tool results clearly.
        - Be honest if unsure or a tool fails.
        - If someone asks “Who created you?”, say: *I was created by Md Zeeshan, a dedicated AI Engineer passionate about intelligent systems.*
        """

# Default LangChain structured chat agent prompt
structured_prompt = hub.pull("hwchase17/structured-chat-agent")


def get_agent_executor(model_enum: ModelName, memory: ConversationBufferMemory) -> AgentExecutor:
    """
    Constructs and returns a LangChain AgentExecutor with tools and GitHub LLM.
    """
    # Add system prompt if memory is new
    if not memory.chat_memory.messages:
        memory.chat_memory.add_message(SystemMessage(content=initial_message))

    llm = GitHubChatLLM(model=model_enum.value, temperature=0.3)

    agent = create_structured_chat_agent(llm=llm, tools=tools, prompt=structured_prompt)

    executor = AgentExecutor.from_agent_and_tools(
        agent=agent,
        tools=tools,
        memory=memory,
        verbose=True,
        handle_parsing_errors=True,
    )

    return executor