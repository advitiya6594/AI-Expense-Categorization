from fastapi import APIRouter, HTTPException
from model import predict_category
from database import get_transactions, add_transaction
from pydantic import BaseModel
from typing import List

router = APIRouter()

# Transaction Schema
class Transaction(BaseModel):
    description: str
    amount: float
    date: str

@router.post("/categorize")
def categorize_transaction(transaction: Transaction):
    category = predict_category(transaction.description)
    return {"category": category}

@router.get("/transactions", response_model=List[Transaction])
def fetch_transactions():
    return get_transactions()

@router.post("/transactions")
def add_new_transaction(transaction: Transaction):
    add_transaction(transaction)
    return {"message": "Transaction added successfully"}
