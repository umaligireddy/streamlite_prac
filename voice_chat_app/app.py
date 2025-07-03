import os
import json
from openai import OpenAI
from dotenv import load_dotenv
import streamlit as st
import re
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)
templates = {
    "Poem": "Write a 4-line poem about {topic}.",
    "Ad": "Create a catchy ad for {product} that solves {problem}.",
    "Resume": "Write a professional summary for a {profession} with {years} years of experience."
}
st.title("prompt templates selector")
st.subheader("chose a template")
template_choice=st.selectbox("select a teplate", list(templates.keys()))
selected_template = templates[template_choice]
fields =re.findall(r"{(.*?)}", selected_template)
input = {}
for field in fields:
    input[field] = st.text_input(f"enter {field}")
if st.button("generate response"):
    if all(input.values()):
        final_prompt = selected_template.format(**input)
        st.write(f"sending this prompt to ChatGPT: {final_prompt}")
        response = client.chat.completions.create(
            model ="gpt-3.5-turbo",
            messages=[{"role":"user","content": final_prompt}]
        )
        reply = response.choices[0].message.content
        st.success(f"chatGPT says: {reply}")
        log ={
            "template": selected_template,
            "filled_prompt": final_prompt,
            "response": reply
        }
        with open("template_chat_log.json", "a", encoding="utf-8") as f:
            json.dump(log,f,indent=4)
            f.write("\n")
            st.success("logged to template_chat_log.json")
    else:
        st.error("please fill all the fields")