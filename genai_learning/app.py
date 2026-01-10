from fastapi import FastAPI
from groq import Groq
from pydantic import BaseModel
import uvicorn
# from main import chatbot

from env import api_key, llama_model
from prompt import prompt

app = FastAPI()

class userMessage(BaseModel):
    message : str


def chatbot(message):
    client = Groq(api_key=api_key)
    completion = client.chat.completions.create(
        model= llama_model,
        messages=[
        {
            "role": "system",
            "content": prompt
        },
        {
            "role": "user",
            "content": message
        }
        ],
        temperature=1,     # it gives random or creative answers, the more the temp the more your answer is different than static or previous one 
        max_completion_tokens=1024,   # It is for how long your output would be or length of the output   
                                      # Approximately 1 token = 0.75 word  i.e 100 tokens = 75 words
        top_p=1,
        stream=False,
        stop=None
    )
    return completion.choices[0].message.content

@app.post("/user-message") 
def respond(message:userMessage):
    response = chatbot(message.message)
    return{
        "result": response
    }


if __name__ == "__main__":
    uvicorn.run("app:app", port=8000, reload= True)
 