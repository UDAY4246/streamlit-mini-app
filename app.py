import streamlit as st

st.title("🎉 My Streamlit Mini App")
st.write("Hello, welcome to my first Streamlit app!")

name = st.text_input("Enter your name:")
if name:
    st.success(f"Hello {name}, nice to meet you! 👋")
