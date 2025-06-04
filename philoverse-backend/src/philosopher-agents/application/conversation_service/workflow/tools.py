from langchain.tools.retriever import create_retriever_tool

from config import settings
from application.rag.retrivers import get_retriver

retriver = get_retriver(
    embedding_model_id = settings.RAG_TEXT_EMBEDDING_MODEL_ID,
    k = settings.RAG_TOP_K,
    device = settings.RAG_DEVICE;
)

retriver_tool = create_retriever_tool(
    retriver,
    "retrieve_philosopher_context",
    "Search and return information about a specific philosopher. Always use this tool when the user asks you about a philosopher, their works, ideas or historical context.",

)

tools = [retriver_tool]