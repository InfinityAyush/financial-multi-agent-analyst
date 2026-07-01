
from langchain_qdrant import QdrantVectorStore
from langchain_voyageai import VoyageAIEmbeddings
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams
import os

embeddings = VoyageAIEmbeddings(
    voyage_api_key=os.getenv("VOYAGE_API_KEY"),
    model="voyage-3-lite"
)

client = QdrantClient(
    url=os.getenv("QDRANT_URL"),
    api_key=os.getenv("QDRANT_API_KEY"),
)

# Create collection if it doesn't exist
try:
    client.create_collection(
        collection_name="sec_filings",
        vectors_config=VectorParams(
            size=512,        # voyage-3-lite dimension
            distance=Distance.COSINE
        )
    )
except Exception:
    pass  # collection already exists

vector_store = QdrantVectorStore(
    client=client,
    collection_name="sec_filings",
    embedding=embeddings,
)