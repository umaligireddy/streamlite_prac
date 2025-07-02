import streamlit as st
import pandas as pd
st.title("file uploder")
uploaded_file = st.file_uploader("choose a file", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("file uploaded successfully")
    st.subheader("data preview")
    st.dataframe(df)
    numeric_columns = df.select_dtypes(include=["float64", "int64"]).columns.tolist()
    if numeric_columns:
        selected_column = st.selectbox("select a numeric column to plot", numeric_columns)
        chart_type = st.radio("select chart type",["bar chart","line chart"])
        st.subheader("chart")
        if chart_type =="bar cart":
            st.bar_chart(df[selected_column])
        else:
            st.line_chart(df[selected_column])
    else:
        st.warning("no numeric column is selected to plot")
else:
    st.warning("please upload a cvs file")