from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

items = ["apple", "banana", "orange"]


#Server health
@app.get("/")
def apphealth():
    return {
        "status": "200 OK"
    }


#Add a new item
class Item(BaseModel):
    name: str


@app.post("/items")
def create_item(item: Item):
    items.append(item)
    return {
        "Item added": item
    }


@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int) -> str:
    """
      Retrieves an item from the list based on its ID.

      Args:
          item_id (int): The integer ID of the item to retrieve.
                         This ID corresponds to the index in the 'items' list.

      Returns:
          str: The item at the specified index.

      Raises:
          HTTPException: If the item_id is negative or out of bounds
                         of the 'items' list, a 404 Not Found error is raised.
      """
    if item_id < len(items):
        return items[item_id]
    else:
        raise HTTPException(status_code=404, detail=f'Item {item_id} not found, Try again')


@app.get("/items", response_model=list[Item])
def list_items(limit: int = 10):
    """
      Lists a subset of items from the list.

      Args:
          limit (int): The maximum number of items to return.
                       Default to 10.

      Returns:
          list: A list containing the specified number of items.
      """
    return items[0: limit]
