
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('YARDAS_PASOS_DATOS_TICS.xlsx', index_col=0)
st.title('Este es un analisis estadistico')
st.header('Base de datos de Yardas vs. pases')
st.dataframe(df.head())

st.header('Estadistica descriptiva.')
st.dataframe(df.describe())

df.columns = [c.lower().replace(' ', '_') for c in df.columns]

fig, ax = plt.subplots()
ax.boxplot(df['yardas_totales'])
st.header("Diagrama de caja y bigote\nde yardas totales")
st.pyplot(fig)



fig, ax = plt.subplots()
ax.boxplot(df['pases_completos'])
st.header("Diagrama de caja y bigote\nde yardas totales")
st.pyplot(fig)


col1, col2 = st.columns(2)

with col1:
    #Este es el diagrama de caja y bigote de los pases completos
    fig, ax = plt.subplots()
    ax.boxplot(df['yardas_totales'])
    st.header("Diagrama de caja y bigote\nde Yardas totales")
    st.pyplot(fig)
with col2:
    #Este es el diagrama de caja y bigote de los pases completos.
    fig, ax = plt. subplots()
    ax.boxplot(df['pases_completos'])
    st.header("Diagrama de caja y bigote\nde Yardas totales")
    st.pyplot(fig)
