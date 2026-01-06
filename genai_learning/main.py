from fastapi import FastAPI
from groq import Groq
from pydantic import BaseModel
import uvicorn

from env import api_key, llama_model
from prompt import prompt


def chatbot(message):
    client = Groq(api_key=api_key)
    completion = client.chat.completions.create(
        model= llama_model,
        messages=[
        {
            "role": "user",
            "content": prompt
        },
        {
            "role": "user",
            "content": message
        }
        ],
        temperature=1,
        max_completion_tokens=1024,
        top_p=1,
        stream=False,
        stop=None
    )
    return completion.choices[0].message.content
# for chunk in completion:
#     print(chunk.choices[0].delta.content or "", end="")



# @app.post("/user-message") 
# def respond(message:userMessage):
#     response = chatbot(message.message)
#     return{
#         "result": response
#     }


# if __name__ == "__main__":
#     uvicorn.run("app:app", port=8000, reload= True)


