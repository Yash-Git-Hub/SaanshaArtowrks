import streamlit as st 
import pandas as pd 


st.markdown("""Saansha Artworks Data""")

df=pd.read_csv("./Data.csv")
st.write(df)