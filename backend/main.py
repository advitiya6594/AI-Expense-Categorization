from fastapi import FastAPI, HTTPException
from api import router as api_router
from database import init_db

app = FastAPI(title="AI Expense Categorization API")

# Include the API router
app.include_router(api_router)

@app.on_event("startup")
def startup():
    init_db()

@app.get("/")
def read_root():
    return {"message": "Welcome to AI-Powered Expense Categorization System"}
