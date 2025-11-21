import requests
import json

def analyze_text_with_ollama(text: str):
    """
    Sends a journal entry to Ollama (Phi3.5) and returns the final combined output.
    """

    url = "http://localhost:11434/api/generate"

    # We force a predictable JSON output so you can parse it later
    prompt = f"""
Analyze this journal entry and return a JSON object with the fields:
- mood: user's emotional state
- summary: a short summary of what they wrote
- suggestion: one practical wellbeing suggestion

Journal entry:
{text}

Respond ONLY with JSON. No extra text.
"""

    payload = {
        "model": "phi3.5",
        "prompt": prompt,
        "stream": True
    }

    # Streaming response from Ollama
    response = requests.post(url, json=payload, stream=True)

    full_text = ""
    for line in response.iter_lines():
        if line:
            data = json.loads(line.decode("utf-8"))
            full_text += data.get("response", "")

    # Sometimes the model adds extra whitespace
    return full_text.strip()
