import requests
import json
from env import backendurl
import streamlit as st

url = backendurl

def callBackend():
    payload = json.dumps({
    "message": user_message
    })
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return json.loads(response.text)

# print(callBackend("Can we reschedule our call to 3 PM?"))


st.title("spam/ham classifier")

user_message = st.text_input("Enter the message to be analyzed")

if st.button("Analyze"):
    if user_message:
        response = callBackend()
        st.write(response["result"])