import streamlit as st
import pandas as pd
import numpy as np

# Title
st.title("🎉 My Streamlit Mini App")
st.write("Hello, welcome to my improved Streamlit app!")

# User input
name = st.text_input("Enter your name:")
if name:
    st.success(f"Hello {name}, nice to meet you! 👋")

# Show an image
st.subheader("📷 Random Image")
st.image("https://picsum.photos/500/250", caption="Here is a random image from Picsum")

# File uploader
st.subheader("📂 File Upload")
uploaded_file = st.file_uploader("Upload a CSV file")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("✅ File uploaded successfully!")
    st.dataframe(df.head())  # show first 5 rows

# Random chart
st.subheader("📊 Random Data Chart")
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A', 'B', 'C']
)
st.line_chart(chart_data)
