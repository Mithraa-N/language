import json, random

with open("backend/chatbot/intents.json", "r", encoding="utf-8") as f:
    intents = json.load(f)

def get_response(message):
    for intent in intents["intents"]:
        if any(kw in message.lower() for kw in intent["keywords"]):
            return random.choice(intent["responses"]), intent["tag"]
    return "I’m not sure. Please contact the admin office.", "fallback"
