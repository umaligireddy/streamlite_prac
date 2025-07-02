import streamlit as st
st.title("Expander")
with st.expander("click to see more"):
    st.write("here you can see the hidden content inside the expander")
    st.image("https://static.streamlit.io/examples/cat.jpg", width=150)