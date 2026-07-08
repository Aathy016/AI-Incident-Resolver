import os
from pathlib import Path

from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError(
        "GOOGLE_API_KEY not found. Add it to your .env file."
    )

print("Gemini API Key Loaded Successfully")

documents = []

runbooks_path = Path("data/runbooks")

for file in runbooks_path.glob("*.txt"):
    loader = TextLoader(
        str(file),
        encoding="utf-8"
    )
    documents.extend(loader.load())

print(f"Documents Loaded: {len(documents)}")

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = splitter.split_documents(documents)

print(f"Chunks Created: {len(chunks)}")

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


db = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="chroma_db"
)

print("Knowledge Base Created Successfully")
print("ChromaDB Saved to: chroma_db/")