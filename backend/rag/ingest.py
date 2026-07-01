from langchain_community.document_loaders import PyPDFLoader

from langchain_text_splitters import RecursiveCharacterTextSplitter
from backend.rag.vector_store import vector_store


def ingest_pdf(file_path: str):

    loader = PyPDFLoader(file_path)

    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(
        documents
    )

    vector_store.add_documents(chunks)

    print(f"Ingested {len(chunks)} chunks")