import pandas as pd  
import matplotlib.pyplot as plt
import streamlit as st

st.header("Dados da empresa 1")

arquivo = "https://raw.githubusercontent.com/WesleyInfoBr2/aula_teste/main/empresa1.csv" 
dfe = pd.read_csv(arquivo, sep=';') 
st.dataframe(dfe)

fig, ax = plt.subplots()
dfe.plot()
st.pyplot(fig)

fig, ax = plt.subplots()
dfe.plot(kind = 'scatter', x = 'EBITDA', y = 'Lucro operacional')
st.pyplot(fig)

fig, ax = plt.subplots()
dfe["Lucro do período"].plot(kind = 'hist')
st.pyplot(fig)


st.write(dfe.groupby('Ano').mean())
