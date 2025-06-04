from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", extra="ignore", env_file_encoding="utf-8"
    )

    """GROQ Information"""
    GROQ_API_KEY :str
    GRQO_LLM_MODEL :str = "llama-3.3-70b-versatile"
    GROQ_LLM_MODEL_CONTEXT_SUMMARY: str = "llama-3.1-8b-instant"


    """OPENAI Configuration"""
    OPENAI_API_KEY :str

    """MONGODB Configuration"""
    MONGO_URI :str = Field(
        default = "",
        description="Connection URI with MongoDB Atlas"

    )

    MONGO_DB_NAME :str = "philoverse"
    MONGO_STATE_CHECKPOINT_COLLECTION :str = "philosopher_state_checkpoints"
    MONGO_STATE_WRITE_COLLECTION :str = "philosopher_state_writes"
    MONGO_LONG_TERM_COLLECTION :str = "philosopher_long_term_memory"

    """COMET ML & OPIK Configuration"""
    COMET_API_KEY : str| None = Field(
        default=None,
        description="API key for Comet ML and Opik services."
    )



    """Agents Configuration"""
    TOTAL_MESSAGES_SUMMARY_TRIGGER :int = 25
    TOTAL_MESSAGES__AFTER_SUMMARY :int = 5



    """RAG Configuration"""
    
    
    RAG_DEVICE :str = "cpu"
    RAG_CHUNK_SIZE :int = 256
    RAG_TEXT_EMBEDDING_MODEL_ID :str = "sentence-transformers/all-MiniLM-L6-v2"
    RAG_TOP_K :int = 5
    RAG_TEXT_EMBEDDING_MODEL_DIMENSIONS :int = 384



    """Paths Configuration"""

    EVALUATION_DATASET_FILE_PATH :Path = Path("data/evaluation_dataset.json")
    EXTRACTION_META_DATA_FILE_PATH :Path = Path("data/extraction_metadata.json")



settings = Settings()