from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

app = FastAPI()

items = [
    {"id": 1, "name": "Item 1"},
    {"id": 2, "name": "Item 2"}
]

class Item(BaseModel):
    name: str

@app.get("/")
def get_items():
    return {"items": items}

@app.get("/{item_id}")
def get_item(item_id: int):
    item = next((item for item in items if item["id"] == item_id), None)
    if item:
        return {"item": item}
    raise HTTPException(status_code=404, detail="Item not found")

@app.post("/", status_code=201)
def create_item(item: Item):
    new_item = {"id": len(items) + 1, "name": item.name}
    items.append(new_item)
    return {"item": new_item}

@app.put("/{item_id}")
def update_item(item_id: int, item_data: Item):
    item = next((item for item in items if item["id"] == item_id), None)
    if item:
        item["name"] = item_data.name
        return {"item": item}
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/{item_id}")
def delete_item(item_id: int):
    global items
    items = [item for item in items if item["id"] != item_id]
    return {"result": True}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)