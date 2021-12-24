import streamlit as st
import pandas as pd 
import plotly.express as px
description = "My first app"
import datetime
def run():

   st.sidebar.title("Saansha Rocks")
   url='https://raw.githubusercontent.com/Yash-Git-Hub/SaanshaArtworks/main/Data.csv'

   df=pd.read_csv(url,index_col=0)
   df['Time']= pd.to_datetime(df['Time'])
   print(df.dtypes)

   st.title ("LETS SELL SOME SUPER ULTRA MEGA PLANNERS")
   st.write(df)
   st.write(px.scatter(df, y="Ranking", x="Time"))




if __name__ == "__main__":
   run()
