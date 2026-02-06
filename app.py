from flask import Flask, request, jsonify, send_from_directory
import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, static_folder='.')

# Configuration
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY") # Securely load from env
SITE_URL = "https://api.groq.com/openai/v1/chat/completions"
RESUME_FILE = "resume_content.txt"

def get_resume_content():
    try:
        with open(RESUME_FILE, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "Resume content not available."

RESUME_CONTEXT = get_resume_content()

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('.', path)

@app.route('/chat', methods=['POST'])
def chat():
    # Reload context on every request to support "retraining"
    resume_context = get_resume_content()
    
    data = request.json
    user_message = data.get('message', '')

    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    system_prompt = f"""You are a helpful AI assistant for Charles Bloomberg's portfolio website. 
    Answer questions based ONLY on the following resume content. 
    If you don't know the answer strictly from the context, say you don't know. 
    Keep answers concise and professional.
    
    RESUME CONTEXT:
    {resume_context}
    """

    payload = {
        "model": "llama-3.1-8b-instant",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ]
    }

    try:
        response = requests.post(SITE_URL, headers=headers, json=payload)
        response.raise_for_status()
        result = response.json()
        bot_reply = result['choices'][0]['message']['content']
        return jsonify({"reply": bot_reply})
    except Exception as e:
        print(f"Error calling OpenRouter: {e}")
        # Fallback error message (or simple echo for debugging if offline)
        return jsonify({"reply": "Sorry, I'm having trouble connecting to my brain right now."}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
