from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

from main import chatbot


app = FastAPI()

class userMessage(BaseModel):
    message : str


@app.post("/user-message") 
def respond(message:userMessage):
    response = chatbot(message.message)
    return{
        "result": response
    }


if __name__ == "__main__":
    uvicorn.run("app:app", port=8000, reload= True)
