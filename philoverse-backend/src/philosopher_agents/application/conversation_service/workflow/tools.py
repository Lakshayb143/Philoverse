from langchain.tools.retriever import create_retriever_tool

from philosopher_agents.config import settings
from philosopher_agents.application.rag.retrievers import get_retriever

retriver = get_retriever(
    embedding_model_id = settings.RAG_TEXT_EMBEDDING_MODEL_ID,
    k = settings.RAG_TOP_K,
    device = settings.RAG_DEVICE,
)

retriver_tool = create_retriever_tool(
    retriver,
    "retrieve_philosopher_context",
    "Search and return information about a specific philosopher. Always use this tool when the user asks you about a philosopher, their works, ideas or historical context.",

)

tools = [retriver_tool]