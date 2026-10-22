import streamlit as st
import pandas_demo as pd

st.header("Data Table Demo")

data = {
    "name": ["Alice", "Bob"],
    "score": [80, 90]
}

df = pd.DataFrame(data)
st.dataframe(df)

st.header("Image Demo")
st.image("crops.jpg", caption="Village Crops")