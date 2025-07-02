import streamlit as st
import pandas as pd
st.title("file uploder")
uploaded_file = st.file_uploader("choose a file", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("file uploaded successfully")
    st.subheader("data preview")
    st.dataframe(df)