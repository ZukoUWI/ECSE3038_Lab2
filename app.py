from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "https://ecse-week3-demo.netlify.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

fake_database = []

@app.get("/todos")
async def get_all_todos():
  return fake_database

@app.post("/todos")
async def create_todo(request: Request):
  todo = await request.json()
  fake_database.append(todo)
  return todo


@app.delete("/todos/{id}")
async def delete_todo(id: int):
    for i, todo in enumerate(fake_database):
        if todo["id"] == id: 
            # Pop used to remove the Item added to the stack      
            fake_database.pop(i)
            return {"message": "Todo with id {} was deleted.".format(id)}
    return {"message": "Todo with id {} not found.".format(id)}    


@app.patch("/todos/{id}")
async def update_todo(id: int, request: Request):
    for i, todo in enumerate(fake_database):
        if todo["id"] == id: 
            #Updates the status of the todo item (True/False)
            updated_todo = await request.json()
            fake_database[i].update(updated_todo)
            return {"message": "Todo with id {} was updated.".format(id)}
    return {"message": "Todo with id {} not found.".format(id)}