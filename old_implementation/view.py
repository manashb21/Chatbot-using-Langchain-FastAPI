import streamlit as st
import httpx
import requests

url = "http://127.0.0.1:8000/stream"

async def chatbot_layout():
    st.title("Hello I am Axle!")

    # Input box for user to type messages
    user_input = st.text_input("How can I help you?", "")

    # Button to submit the message
    if st.button("Send"):
        st.write(f"User: {user_input}")

        # Send a POST request to a server
        # post_data = {"message": user_input}
        # response = requests.post("http://127.0.0.1:8000/stream", json=post_data)

        # st.text_area("Chatbot's Reply:", response.text, height=100)
        post_data = {"message": user_input}
        await fetch_stream(url, post_data)

async def fetch_stream(url, post_data):
    async with httpx.AsyncClient() as client:
        async with client.post(url, json=post_data, timeout=None, stream=True) as response:
            async for chunk in response.aiter_text():
                st.text(chunk)


# Display the chatbot layout
chatbot_layout()
