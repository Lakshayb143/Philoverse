from langchain_huggingface import HuggingFaceEmbeddings
from langchain_mongodb import MongoDBAtlasVectorSearch
from langchain_mongodb.retrievers import(
    MongoDBAtlasHybridSearchRetriever
)

from loguru import logger

from philosopher_agents.config import settings

from philosopher_agents.application.rag.embeddings import get_embedding_model

Retriever = MongoDBAtlasHybridSearchRetriever


def get_retriever(embedding_model_id :str, k :int = 3, device :str = "cpu") -> Retriever:
    """Creates and returns a hybrid search retriever with the specified embedding model
    

    Returns:
        Retriever: A configured hybrid search retriever
    
    """

    logger.info(
        f"Initializing retriever | model: {embedding_model_id} | device: {device} | top_k: {k}"
    )

    embedding_model = get_embedding_model(embedding_model_id, device)

    return get_hybrid_search_retriever(embedding_model, k)


def get_hybrid_search_retriever(embedding_model :HuggingFaceEmbeddings, k :int) -> MongoDBAtlasHybridSearchRetriever:
    """
    Creates a MongoDB Atlas hybrid search retriever with the given embedding model.

    Returns:
        MongoDBAtlasHybridSearchRetriever: A configured hybrid search retriever using both
        vector and text search capabilities.
    """

    vector_store = MongoDBAtlasVectorSearch.from_connection_string(
        connection_string= settings.MONGO_URI,
        embedding=embedding_model,
        namespace=f"{settings.MONGO_DB_NAME}.{settings.MONGO_LONG_TERM_COLLECTION}" ,
        text_key = "chunk",
        embedding_key = "embedding",
        relevance_score_fn = "dotProduct",
        
    )

    retriever = MongoDBAtlasHybridSearchRetriever(
        vector_store= vector_store,
        search_index_name = "hybrid_search_index",
        top_k = k,
        vector_penalty = 50,
        fulltext_penalty= 50,
    )

    return retriever










