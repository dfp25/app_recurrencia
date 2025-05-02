#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import numpy as np
import pandas as pd
import lightgbm as lgb
import joblib
import plotly.graph_objects as go
import sklearn


def color_verde(pct):
    intensidad = int(255 * (pct / 100))  # De 0 a 255.
    return f"rgb(0, {intensidad}, 0)"  # Intensidad variable del verde.


# Configuración de la página
st.set_page_config(page_title="Fidelización Cliente", page_icon="⚙️", layout="wide")
st.title(":rainbow[_Predicción de Recurrencia del Cliente_]")
st.subheader("Clasificación binaria basada en LightGBM")

# Cargar el modelo entrenado en caché (evitamos recargar continuamente el modelo)
@st.cache_resource
def cargar_modelo():
    return joblib.load("modelo_recurrencia_7.joblib")

modelo = cargar_modelo()['modelo']  # El modelo se guardó como diccionario.

# Sidebar con entradas del usuario
with st.sidebar:
    st.write("### Parámetros del modelo")

    # Variables de entrada # Ejemplos: [Mínimo, Máximo, Media]
    n_productos_distintos = st.slider(
        "1-Número de productos únicos consultados (media = 1.04)", 0, 7)                      #  [0, 7, 1.04]
    dias_consulta = st.slider(
        "2-Días transcurridos entre la primera y última consulta (media = 122.39)", 0, 2291)  #  [0, 2291, 122.39]
    consultas_por_dia = st.slider(
        "3-Consultas promedio por día activo (media = 1.76)", 0, 436)                         #  [0, 435.58, 1.76]
    consumos_total = st.slider(
        "4-Número total de consultas realizadas (media = 101.61)", 1, 371738)                 #  [1, 371738, 101.61]
    empresas_unicas_consult = st.slider(
        "5-Número de empresas únicas consultadas (media = 50.52)", 1, 154069)                 #  [1, 154069, 50.52]
    dias_distintos_consulta = st.slider(
        "6-Número de días distintos en los que hay consultas (media = 4.60)", 0, 1816)        #  [0, 1816, 4.60]
    n_sectores_distintos = st.slider(
        "7-Número de sectores distintos consultados (media = 1.30)", 0, 22)                   #  [0, 22, 1.30]

    ejecutar = st.button(":orange[PREDECIR PROBABILIDADES]")


if ejecutar:
    # Crear dataframe con los inputs en el mismo orden que el entrenamiento
    entrada = pd.DataFrame([[
        n_productos_distintos,
        dias_consulta,
        consultas_por_dia,
        consumos_total,
        empresas_unicas_consult,
        dias_distintos_consulta,
        n_sectores_distintos
        ]], columns=[
        'n_productos_distintos',
        'dias_consulta',
        'consultas_por_dia',
        'consumos_total',
        'empresas_unicas_consult',
        'dias_distintos_consulta',
        'n_sectores_distintos'
        ])

    # Predicción
    probs = modelo.predict_proba(entrada)[0]  # Ejemplo: [0.30, 0.70]

    # Separación de predicción
    st.markdown("---")

    # Clase
    clase_predicha = 1 if probs[1] > probs[0] else 0
    texto = "Cliente recurrente ✅" if clase_predicha == 1 else "Cliente No recurrente ❌"
    color = "green" if clase_predicha == 1 else "red"

    # Mostrar etiqueta de predicción con color
    st.markdown(f"<h3 style='color:{color}'>🧐 Predicción: {texto}</h3>", unsafe_allow_html=True)

    # Mostrar velocímetros con Plotly uno al lado del otro
    col1, col2 = st.columns(2)

    with col1:
        valor0 = probs[0] * 100
        st.plotly_chart(go.Figure(go.Indicator(
            mode="gauge+number",
            value=probs[0]*100,
            number={'suffix': '%'},
            title={'text': "Cliente NO recurrente (clase 0)"},
            gauge={'axis': {'range': [0, 100]},
                   'bar': {'color': color_verde(valor0)}
                   }
            )), use_container_width=True)

    with col2:
        valor1 = probs[1] * 100
        st.plotly_chart(go.Figure(go.Indicator(
            mode="gauge+number",
            value=probs[1]*100,
            number={'suffix': '%'},
            title={'text': "Cliente recurrente (clase 1)"},
            gauge={'axis': {'range': [0, 100]},
                   'bar': {'color': color_verde(valor1)}
                   }
            )), use_container_width=True)
else:
    st.subheader("_Introduce los datos y haz click en_ :orange[_PREDECIR PROBABILIDADES_]")

