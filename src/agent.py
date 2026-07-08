import os

from dotenv import load_dotenv
from langgraph.graph import StateGraph
from langchain_google_genai import ChatGoogleGenerativeAI

from src.rag_engine import search_runbook

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)


def analyze(state):

    issue = state["issue"]

    knowledge = search_runbook(issue)

    prompt = f"""
You are an Enterprise SRE AI Assistant.

Incident:
{issue}

Knowledge Base:
{knowledge}

Provide:

1. Root Cause Analysis
2. Impact
3. Resolution Steps
4. Prevention Recommendations
"""

    response = llm.invoke(prompt)

    return {
        "issue": issue,
        "knowledge": knowledge,
        "result": response.content
    }


workflow = StateGraph(dict)

workflow.add_node(
    "analyzer",
    analyze
)

workflow.set_entry_point(
    "analyzer"
)

workflow.set_finish_point(
    "analyzer"
)

app = workflow.compile()


if __name__ == "__main__":

    result = app.invoke(
        {
            "issue": "Database connection timeout"
        }
    )

    print(result["result"])