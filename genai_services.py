import os
import requests
from dotenv import load_dotenv

load_dotenv()

MODEL_BASE_URL = os.getenv("MODEL_BASE_URL")
MODEL_API_KEY = os.getenv("MODEL_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME")

def answer_with_context(prompt, context=""):
    url = f"{MODEL_BASE_URL}/{MODEL_NAME}:generateContent?key={MODEL_API_KEY}"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "contents": [
            {
                "role": "user",
                "parts": [
                    {"text": f"{context}\n\n{prompt}"}
                ]
            }
        ]
    }
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    result = response.json()
    try:
        return result["candidates"][0]["content"]["parts"][0]["text"]
    except Exception:
        return "No response from Gemini API."

def summarize_text(text):
    prompt = "Summarize the following text:"
    return answer_with_context(prompt, context=text)

def chunk_text(text, chunk_size=1000):
    # Simple chunking by character count
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]