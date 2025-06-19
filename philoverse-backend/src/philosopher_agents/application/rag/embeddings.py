from langchain_huggingface import HuggingFaceEmbeddings

EmbeddingsModel = HuggingFaceEmbeddings

def get_embedding_model(model_id :str, device :str = "cpu") -> EmbeddingsModel:
    """
    Create a instance of a HuggingFace embedding model


    Returns:
        EmbeddingModel : A configured HuggingFace embeddings model instance
    
    """

    return get_huggingface_embedding_model(model_id, device)



def get_huggingface_embedding_model(model_id :str, device :str) -> HuggingFaceEmbeddings:
    """
    Gets a HuggingFace embedding model instance.

    Returns:
        HuggingFaceEmbeddings: A configured HuggingFace embeddings model instance
        with remote code trust enabled and embedding normalization disabled
    """

    return HuggingFaceEmbeddings(
        model_name=model_id,
        model_kwargs={"device":device, "trust_remote_code" :True},
        encode_kwargs={"normalize_embeddings": False},
    )
