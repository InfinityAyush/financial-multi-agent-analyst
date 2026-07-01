from backend.rag.retriever import retriever
from backend.config.llm_router import get_llm

llm = get_llm()


def sec_rag_agent(question: str):

    docs = retriever.invoke(question)

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
You are a senior financial analyst.

Answer ONLY using the SEC filing context.

SEC Filing Context:
{context}

Question:
{question}

Generate a report containing:

1. Business Overview
2. Key Risks
3. Growth Opportunities
4. Long-Term Outlook

Mention evidence from the SEC filing.
"""

    response = llm.invoke(prompt)

    return response.content