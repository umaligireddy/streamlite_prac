import streamlit as st
st.title("layout with columns")
col1,col2= st.columns(2)
with col1:
    st.header("column 1")
    st.subheader("this is column 1")
with col2:
    st.header("column2")
    st.subheader("this is column 2")
    