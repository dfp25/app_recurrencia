#!/usr/bin/env python
# coding: utf-8

# In[5]:


import streamlit as st
import pandas as pd
import lightgbm as lgb
import joblib
import plotly.graph_objects as go

# Configuración de la página
st.set_page_config(page_title="Predicción ML - LightGBM", page_icon="⚙️", layout="wide")
st.title(":rainbow[_Predicción de Probabilidades con LightGBM_]")
st.subheader("Clasificación binaria basada en entradas del usuario")

# Cargar el modelo entrenado en caché (evitamos recargar continuamente el modelo)
@st.cache_resource
def cargar_modelo():
    return joblib.load("modelo_recurrencia_7.joblib")

modelo = cargar_modelo()['modelo']  # El modelo se guardó como diccionario.

# Sidebar con entradas del usuario
with st.sidebar:
    st.image("logo vencex portada - 240x60.png", output_format="PNG")

    st.write("### Parámetros del modelo")

    # Variables de entrada # Ejemplos: [Mínimo, Máximo, Media]
    n_productos_distintos = st.slider(
        "Número de productos únicos consultados", 0, 100)                 #  [0, 7, 1.04]
    dias_consulta = st.slider(
        "Días transcurridos entre la primera y última consulta", 0, 100)  #  [0, 2291, 122.39]
    consultas_por_dia = st.slider(
        "Consultas promedio por día activo", 0.0, 50.0)                   #  [0, 435.58, 1.76]
    consumos_total = st.slider(
        "Número total de consultas realizadas", 0.0, 10000.0)             #  [1, 371738, 101.61]
    empresas_unicas_consult = st.slider(
        "Número de empresas únicas consultadas", 0, 100)                  #  [1, 154069, 50.52]
    dias_distintos_consulta = st.slider(
        "Número de días distintos en los que hay consultas", 0, 100)      #  [0, 1816, 4.60]
    n_sectores_distintos = st.slider(
        "Número de sectores distintos consultados", 0, 50)                #  [0, 22, 1.30]

    if st.button("PREDECIR PROBABILIDADES"):
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

        # Mostrar velocímetros con Plotly
        col1, col2 = st.columns(2)

        with col1:
            st.plotly_chart(go.Figure(go.Indicator(
                mode="gauge+number",
                value=probs[0]*100,
                title={'text': "Probabilidad Clase 0"},
                gauge={'axis': {'range': [0, 100]}}
            )), use_container_width=True)

        with col2:
            st.plotly_chart(go.Figure(go.Indicator(
                mode="gauge+number",
                value=probs[1]*100,
                title={'text': "Probabilidad Clase 1"},
                gauge={'axis': {'range': [0, 100]}}
            )), use_container_width=True)
    else:
        st.subheader(":orange[_Introduce los datos y haz click en_] _PREDECIR PROBABILIDADES_")

