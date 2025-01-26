import streamlit as st
import pandas as pd

df = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSnNn7e3b6WSGzOagWF77LyjNSRg6PJgHZ0No056Mp6w26A-g1AzjBWqJlvYZIPJkDmi-Fq2KDxDhzs/pub?gid=733224137&single=true&output=csv')
df = df.dropna()

#começo
st.write(""" # Registro de Estudos """)
st.button("Disciplina")

st.divider()
#sidebar
st.sidebar.header(" Filtros ")




##
st.data_editor(df)
st.divider()

#Graficos

st.bar_chart(df, x= 'Disciplina', y="Questões Totais")
#fim
