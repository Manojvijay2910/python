import streamlit as st

st.header("Calculator")

num1 = st.number_input("Enter First number:")
num2 = st.number_input("Enter Second number:")

op = st.selectbox("Select Operation:", ["Add", "Subtract", "Multiply", "Divide"])

if st.button("Calculate"):
    if op == "Add":
        result = num1 + num2
    elif op == "Subtract":
        result = num1 - num2
    elif op == "Multiply":
        result = num1 * num2
    elif op == "Divide":
        result = num1 / num2 if num2 != 0 else "can't divide by zero"

    st.success(f"Result: {result}")