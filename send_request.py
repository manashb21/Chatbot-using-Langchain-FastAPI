import requests
import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), 'config', '.env')

load_dotenv(dotenv_path)

url = "http://127.0.0.1:8000/stream"
api_key = os.environ.get("API_KEY")

print(api_key)

headers = {
    "access_token": api_key,
    "Content-Type": "application/json",
}

payload = {
    "message": "Hello"
}

response = requests.post(url, headers=headers, json=payload)

print("Response Status Code:", response.status_code)
print("Response Body:", response.text)
