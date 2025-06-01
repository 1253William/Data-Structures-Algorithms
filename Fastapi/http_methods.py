from fastapi import FastAPI
from pydantic import BaseModel

#Instantiate app
app = FastAPI()

#GET Operation in fastapi
#Handle GET requests to root

@app.get("/")
def root():
    return {
        "message": "An HTTP GET response"
    }

@app.get("/hello")
def hello(name: str = "Alan"):
    return {
        "message": f"Hello {name}"
    }

#POST Operation to make a new music review
class Review (BaseModel):
    rating: int
    review_message: str
    public: bool = False

class MovieReview(BaseModel):
    movie_name: str
    review: Review

class Item(BaseModel):
    name: str

@app.post("/items")
def items(item: Item):
    name: item.name
    return{
        "name": name
    }



