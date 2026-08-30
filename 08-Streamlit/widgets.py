import streamlit as st

st.title("Streamlit text input")

name = st.text_input("Enter your name:")

age = st.slider("Select Your age: ", 0, 100, 25)

option = ["Python", "Java", "Javascript", "c++"]
choice=st.selectbox("Choose your favorite language:", option)
st.write(f"You selected {choice}")

if name:
    st.write(f"Hello, {name}")
    st.write(f"your age is, {age}")
