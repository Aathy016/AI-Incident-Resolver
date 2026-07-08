from fastapi import FastAPI

from src.agent import app

api = FastAPI(
    title="AI Incident Resolver"
)


@api.get("/incident")
def incident(issue: str):

    result = app.invoke(
        {
            "issue": issue
        }
    )

    return result