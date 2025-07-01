
import json

with open("chat.json","r", encoding="utf-8") as file:
    loaded_chats = json.load(file)
for chat in loaded_chats:
    print(f"{chat['user']} asked {chat['prompt']}\nrespons: {chat['response']}")
