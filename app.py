import streamlit as st
import pandas as pd

st.title("Financial Analyst App")

uploaded_file = st.file_uploader(
    "Upload Financial Statement",
    type=["xlsx"]
)

if uploaded_file:

    df = pd.read_excel(uploaded_file)

    st.subheader("Uploaded Data")
    st.dataframe(df)

    st.success("File uploaded successfully!")
  
