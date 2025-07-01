import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
api_key=os.getenv("OPENAI_API_KEY")
client=OpenAI(api_key=api_key)

templates = {
    "poem":"write a 5 line poem for a kid named {name} about {topic}.",
    "ad":"create a catchy ad for {product} that solves {problem}. ",
    "resume":"write a professional summary for someone who is a {profession} with {year} years of experience"
}
print(f"Available prompt Templates:")
for key in templates:
    print(f"{key}")
choice = input("\nwhich template would you like to use?(type 'poem','ad' or 'resume'):").strip().lower()
if choice in templates:
    template= templates[choice]
    fields=[word.strip("{}") for word in template.split() if word.startswith("{")]
    filled = {}
    for field in fields:
        value=input(f"enter {field}:")
        filled[field]=value
    final_prompt =template.format(**filled)
    print(f"sending this prompt to chatGpt: {final_prompt}")
    response= client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user","content": final_prompt}]
    )
    reply=response.choices[0].message.content
    print(f"ChatGpt:{reply}")
    with open("templat_chat_log.json","a",encoding="utf-8") as file:
        json.dump({"template": template, "filled_prompt": final_prompt,"response":reply},file,indent=4)
        file.write("\n")
        print("logged to template_chat_log")
else:
    print("invalid choice,please run again")