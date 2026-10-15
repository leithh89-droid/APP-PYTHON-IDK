import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_excel('YARDAS_PASOS_DATOS_TICS.xlsx', index_col=0)
# df.tail()
st.title("Este es un analisis estadistico")
st.header("base de datos de Yardas vs. Pases")
st.dataframe(df.head())

#Esta es la estadistica descriptiva 
st.header ("estadistica descriptiva")
st.dataframe(df.describe())

#Esto esta estandarizando las columnas 
df.columns = [c.lower().replace(' ', '_') for c in df.columns]
df.head()

#Este es el diagrama y bigote 
# de las yardas totales 
fig,ax = plt.subplots()
ax.boxplot(df['yardas_totales'])
st.header("Diagrama de caja y bigote\nde Yardas totales")
st.pyplot(fig)

#Este es el diagrama y bigote 
# de los pases completos 
fig,ax = plt.subplots()
ax.boxplot(df['pases_completos'])
st.header("Diagrama de caja y bigote\nde Yardas totales")
st.pyplot(fig)

col1, col2 = st.columns(2)
with col1:
    #Este es el diagrama y bigote 
    # de las yardas totales 
    fig,ax = plt.subplots()
    ax.boxplot(df['yardas_totales'])
    st.header("Diagrama de caja y bigote\nde Yardas totales")
    st.pyplot(fig)
with col2:
    #Este es el diagrama y bigote 
    # de los pases completos 
    fig,ax = plt.subplots()
    ax.boxplot(df['pases_completos'])
    st.header("Diagrama de caja y bigote\nde Yardas totales")
    st.pyplot(fig)
    