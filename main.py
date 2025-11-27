from fastapi import FastAPI, Query
from typing import List

app = FastAPI()

messages = [
    {"id": 1, "text": "Hello world"},
    {"id": 2, "text": "Hi there"},
    {"id": 3, "text": "Hello from Symphonic"},
    {"id": 4, "text": "Search API test"},
]

@app.get("/search")
def search_messages(q: str = Query(...), page: int = 1, limit: int = 10):
    results = [m for m in messages if q.lower() in m["text"].lower()]
    start = (page - 1) * limit
    end = start + limit
    return {"results": results[start:end], "total": len(results)}