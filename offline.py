import streamlit as st
import requests
import json

# Define the endpoint URL
url = "http://15.20.18.134:1234/v1/chat/completions"

# Streamlit app title
st.title("LLM Chatbot")

# Input fields for the user to enter their question
user_input = st.text_input("Ask the model a question:")

# If user input is provided, send a request to the model
if user_input:
    # Define the headers
    headers = {
        "Content-Type": "application/json"
    }

    # Define the payload (data to send)
    data = {
        "model": "meta-llama-3.1-8b-instruct",
        "messages": [
            {"role": "system", "content": "Always answer in simple text. Today is Thursday"},
            {"role": "user", "content": user_input}
        ],
        "temperature": 0.7,
        "max_tokens": -1,
        "stream": False
    }

    # Send the POST request
    response = requests.post(url, headers=headers, data=json.dumps(data))

    # Check if the request was successful
    if response.status_code == 200:
        response_data = response.json()
        model_response = response_data['choices'][0]['message']['content']
        st.write(f"**Model's response:** {model_response}")
    else:
        st.error(f"Error: {response.status_code}, {response.text}")
