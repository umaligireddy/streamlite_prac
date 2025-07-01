import streamlit as st
st.title("using sidebar")
name = st.sidebar.text_input("enter your name")
age = st.sidebar.number_input("enter your age", min_value=1, max_value=100)
if st.sidebar.button("submit"):
    st.success(f"hello,{name}! you are {age} years old.")