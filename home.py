import streamlit as st
import pandas as pd


st.title("Website Developing using Python")
st.header("Website Developing using Python")

st.image('./img/monruede.jpg')
st.subheader("Monruede Chomchuen")

dt=pd.read_csv('./data/itis-3.csv')
st.header("ข้อมูลดอกไม้")
st.write(dt.head(10))
