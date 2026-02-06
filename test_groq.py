import requests
import json

GROQ_API_KEY = "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"
SITE_URL = "https://api.groq.com/openai/v1/chat/completions"

def test_groq():
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama-3.1-8b-instant", # Updated model
        "messages": [
            {"role": "user", "content": "Hello! If you can read this, reply with 'Groq API Working'."}
        ]
    }

    print("Sending request to Groq...")
    try:
        response = requests.post(SITE_URL, headers=headers, json=payload)
        
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            bot_reply = result['choices'][0]['message']['content']
            print("\n----- BOT REPLY -----")
            print(bot_reply)
            print("---------------------")
        else:
            print(f"Error: {response.text}")

    except Exception as e:
        print(f"Exception occurred: {e}")

if __name__ == "__main__":
    test_groq()
