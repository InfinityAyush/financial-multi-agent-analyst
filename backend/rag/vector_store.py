
from langchain_chroma import Chroma

from langchain_voyageai import VoyageAIEmbeddings
import os

embeddings = VoyageAIEmbeddings(
    voyage_api_key=os.getenv("VOYAGE_API_KEY"),
    model="voyage-3-lite"   # best free tier model
)

vector_store = Chroma(
    collection_name="sec_filings",
    embedding_function=embeddings,
    persist_directory="./chroma_db"
)