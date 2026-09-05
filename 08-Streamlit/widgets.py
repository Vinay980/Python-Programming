import streamlit as st
import pandas as pd

st.title("Streamlit text input")

name = st.text_input("Enter your name:")

age = st.slider("Select Your age: ", 0, 100, 25)

option = ["Python", "Java", "Javascript", "c++"]
choice=st.selectbox("Choose your favorite language:", option)
st.write(f"You selected {choice}")

if name:
    st.write(f"Hello, {name}")
    st.write(f"your age is, {age}")


data={
    "Name":["John","Jane","Jake","Jill"],
    "Age":[28,29,30,31],
    "City":["New York","Los Angeles","Chicago","Houston"]
}

df=pd.DataFrame(data)
df.to_csv("Sample.csv")
st.write(df)

upload_file=st.file_uploader("Choose a CSV file",type="csv")

if upload_file is not None:
    df=pd.read_csv(upload_file)
    st.write(df)