"""
CRUD Server — FastAPI + in-memory store
Run:  uvicorn crud_server:app --reload
Docs: http://localhost:8000/docs
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, Dict
import uuid

app = FastAPI(title="CRUD Server", version="1.0.0")

# ---------------------------------------------------------------------------
# Data model
# ---------------------------------------------------------------------------

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    in_stock: bool = True

class ItemInDB(Item):
    id: str

# ---------------------------------------------------------------------------
# In-memory "database"
# ---------------------------------------------------------------------------

db: Dict[str, ItemInDB] = {}

# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------

@app.get("/")
def root():
    return {"message": "CRUD Server is running. Visit /docs for the API explorer."}


# CREATE
@app.post("/items", response_model=ItemInDB, status_code=201)
def create_item(item: Item):
    item_id = str(uuid.uuid4())
    record = ItemInDB(id=item_id, **item.model_dump())
    db[item_id] = record
    return record


# READ ALL
@app.get("/items", response_model=list[ItemInDB])
def list_items():
    return list(db.values())


# READ ONE
@app.get("/items/{item_id}", response_model=ItemInDB)
def get_item(item_id: str):
    record = db.get(item_id)
    if not record:
        raise HTTPException(status_code=404, detail="Item not found")
    return record


# UPDATE (full)
@app.put("/items/{item_id}", response_model=ItemInDB)
def update_item(item_id: str, item: Item):
    if item_id not in db:
        raise HTTPException(status_code=404, detail="Item not found")
    updated = ItemInDB(id=item_id, **item.model_dump())
    db[item_id] = updated
    return updated


# PARTIAL UPDATE
@app.patch("/items/{item_id}", response_model=ItemInDB)
def patch_item(item_id: str, item: Item):
    record = db.get(item_id)
    if not record:
        raise HTTPException(status_code=404, detail="Item not found")
    patch_data = item.model_dump(exclude_unset=True)
    updated = record.model_copy(update=patch_data)
    db[item_id] = updated
    return updated


# DELETE
@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: str):
    if item_id not in db:
        raise HTTPException(status_code=404, detail="Item not found")
    del db[item_id]