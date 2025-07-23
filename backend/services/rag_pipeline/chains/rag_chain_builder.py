from backend.services.shared.github_llm import GitHubChatLLM
from backend.services.rag_pipeline.prompts.contexualize_prompt import contextualize_q_prompt
from backend.services.rag_pipeline.prompts.qa_prompt import qa_prompt
from backend.services.rag_pipeline.chroma_utils import vectorstore
from langchain.chains import create_history_aware_retriever, create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain

def get_rag_chain(model="openai/gpt-4o-mini"):
    llm = GitHubChatLLM(model=model)
    retriever = vectorstore.as_retriever(search_kwargs={"k": 2})
    history_aware_retriever = create_history_aware_retriever(llm, retriever, contextualize_q_prompt)
    question_answer_chain = create_stuff_documents_chain(llm, qa_prompt)
    rag_chain = create_retrieval_chain(history_aware_retriever, question_answer_chain)
    return rag_chain
