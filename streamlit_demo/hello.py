import streamlit as st

st.title("Hello Streamlit")
st.write("This is my first streamlit App!")

name = st.text_input("Enter your name")

if st.button("Say Hello"):
    st.success(f"Hello, {name}")