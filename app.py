import streamlit as st
import pandas as pd

st.title("Dashboard de Carros")

df = pd.read_csv("data/vehicles.csv")

st.subheader("Visualização dos Dados")
st.dataframe(df)
