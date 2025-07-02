import streamlit as st
st.title("Richard Taylor's streamlit app")
with st.expander("click to see more"):
    st.write("hay reachard taylor this is your first streamlit app")
    st.image("https://static.streamlit.io/examples/cat.jpg", width=150)
st.subheader("this is columns example")
col1,col2= st.columns(2)
with col1:
    st.write("this is column 1")
    with st.expander("click to see more in column 1"):
        st.write("this is the hidden content in column 1")
with col2:
    st.write("this is column 2")
    with st.expander("click to see more in colunm 2"):
        st.write("this is the hidden content in column 2")