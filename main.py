from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

prompts = [
    "What is Python used for?",
    "Give me 3 weird facts about Mars.",
    "Explain AI like I'm 5.",
    "Who is the president of India?",
    "What is the meaning of life?"
]
with open("chat_log.txt","a",encoding="utf-8") as log_file:
    for i , prompt in enumerate(prompts):
        print(f"\n prompt {i+1}:{prompt}")
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        reply= response.choices[0].message.content
        print("ChatGPT says", reply)
        log_file.write(f"\nprompt {i+1}: {prompt}\n")
        log_file.write(f"response:\n {reply}\n")
        log_file.write("_" * 180)
