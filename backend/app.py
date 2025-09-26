from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from chatbot import nlp, response_handler
import json, datetime

app = FastAPI()

# Allow frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    user_message = data.get("message", "")

    # Step 1: Detect language + translate
    detected_lang, translated_msg = nlp.detect_and_translate(user_message)

    # Step 2: Get intent + response
    response, intent = response_handler.get_response(translated_msg)

    # Step 3: Translate back if needed
    final_response = nlp.translate_to_lang(response, detected_lang)

    # Step 4: Log conversation
    with open("logs/conversations.log", "a", encoding="utf-8") as f:
        f.write(f"{datetime.datetime.now()} | User({detected_lang}): {user_message} | Bot: {final_response}\n")

    return {"response": final_response, "intent": intent}
