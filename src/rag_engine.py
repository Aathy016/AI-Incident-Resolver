from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = Chroma(
    persist_directory="chroma_db",
    embedding_function=embeddings
)

def search_runbook(issue):

    docs = db.similarity_search(
        issue,
        k=3
    )

    if not docs:
        return "No relevant runbook found."

    return "\n\n".join(
        [doc.page_content for doc in docs]
    )


if __name__ == "__main__":

    issue = "Database connection timeout"

    result = search_runbook(issue)

    print("\n=== Retrieved Runbook ===\n")
    print(result)