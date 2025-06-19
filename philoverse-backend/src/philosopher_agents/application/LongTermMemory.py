from langchain_core.documents import Document
from loguru import logger

from philosopher_agents.application.rag.retrievers import Retriever, get_retriever
from philosopher_agents.application.rag.splitters import get_splitter
from philosopher_agents.domain.philosopher import PhilosopherData


from philosopher_agents.config import settings
