from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

qa_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are an intelligent and helpful AI assistant.\n\n"
        "When provided with context from documents, use it to answer the user's question if it's relevant.\n"
        "If the context is missing, unrelated, or doesn't help answer the question, rely on your own general knowledge.\n\n"
        "Guidelines:\n"
        "- If the question relates to the context, use it and summarize or cite as needed.\n"
        "- If not, feel free to answer directly based on what you know.\n"
        "- Do not refuse to answer unless you're truly unsure.\n"
        "- Be clear, helpful, and factually correct."
    ),
    ("system", "Context:\n{context}"),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{input}")
])