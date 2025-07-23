from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

contextualize_q_system_prompt = (
    "You are an AI assistant that helps reformulate user questions for better understanding and retrieval.\n\n"
    "Given a chat history and the latest user query, your task is to rewrite the user's question as a standalone, complete question.\n"
    "The reformulated question should contain all necessary context from the conversation so it can be understood without referring to prior messages.\n\n"
    "Important:\n"
    "- Do NOT answer the question.\n"
    "- Only rewrite the question if needed. If it is already standalone, return it as-is.\n"
    "- Ensure the reformulated version is clear, specific, and self-contained."
)

contextualize_q_prompt = ChatPromptTemplate.from_messages([
    ("system", contextualize_q_system_prompt),
    MessagesPlaceholder("chat_history"),
    ("human", "{input}"),
])