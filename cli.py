import json
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)
name=input("enter your name")
chat_log=[]
while True:
    prompt = input("\n ask your question (or type exit to quit)")
    if prompt.lower() == "exit":
        break
    response=client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role":"user","content": prompt}
        ]
    )
    reply=response.choices[0].message.content
    print(f"chatGPT: {reply}")
    chat={
    "user": name,
    "prompt": prompt,
    "response": reply
    }
    chat_log.append(chat)
with open("chats_log.json","w", encoding="utf-8") as log_json:
    json.dump(chat_log,log_json,indent=4)
