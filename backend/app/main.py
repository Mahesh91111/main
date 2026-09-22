from fastapi import FastAPI

from app.api.v1.auth.router import router as auth_router

app = FastAPI(
    title="AI Medical Hospital"
)

app.include_router(auth_router)


@app.get("/")
def root():
    return {
        "message": "AI Medical Hospital API"
    } 
