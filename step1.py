import streamlit as st
st.title("this is my first step")
st.header("welcome to streamlit first step")
st.subheader("hello umesh reddy")
name=st.text_input("Enter your name")
if st.button("greet me"):
    st.success(f"hello! {name}, welcome here.")