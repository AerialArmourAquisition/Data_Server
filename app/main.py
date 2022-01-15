from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


@app.get("/items/")
async def read_item(start: int = 0, end: int = 10):
    return fake_items_db[start: start + end]


@app.get("/other_items/{item_id}")
async def other_item(item_id: str, q: Optional[str] = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}


@app.post("/items/")
async def create_item(item: Item):
    return item

