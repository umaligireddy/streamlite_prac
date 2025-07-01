import streamlit as st
import os
from openai import OpenAI
from dotenv import load_dotenv
import json
import re

load_dotenv()
api_key=os.getenv("OPENAI_API_KEY")
client=OpenAI(api_key=api_key)
templates ={"Poem": "Write a 5-line poem for a kid named {name} about {topic}.",
    "Ad": "Create a catchy ad for {product} that solves {problem}.",
    "Resume": "Write a professional summary for someone who is a {profession} with {year} years of experience."
    }
st.title("AI prompt template generator")
st.subheader("choose a template and customise it")
template_choice= st.selectbox("select a template",list(templates.keys()))
selected_template =templates[template_choice]
fields=[word.strip("{}") for word in selected_template.split() if word.startswith("{")]
fields=re.findall(r"{(.*?)}", selected_template)
inputs={}
for field in fields:
    inputs[field]=st.text_input(f"enter {field}")
if st.button("genrate response"):
    final_prompt= selected_template.format(**inputs)
    st.info(f"prompt sent : {final_prompt}")
    response= client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user", "content": final_prompt}]
    )
    reply=response.choices[0].message.content
    st.success("ChatGPT Says:")
    st.write(reply)
    log ={
        "template": selected_template,
        "prompt": final_prompt,
        "response": reply
    }
    with open("streamlit_chat_log.json","a",encoding="utf-8") as log_file:
        json.dump(log, log_file, indent=4)
        log_file.write("\n")
    st.caption("logged to streamlit_chat_log.json")
else:
    st.warning("Please fill in all the fields before generating a response.")