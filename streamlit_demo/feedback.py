import streamlit as st

st.title("Feedback Form")
name = st.text_input("Enter your name")
feedback = st.text_input("Enter your feedback")
rating = st.slider("Rating", 1, 5, 3)

if st.button("Submit"):
    st.write("### Thank you for your feedback!")
    st.write(f"Name: {name}")
    st.write(f"Feedback: {feedback}")
    st.write(f"Rating: {rating}")