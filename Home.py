import pandas as pd
import streamlit as st
import utilidades as util


# Activar entorno: .\.venv\Scripts\activate
# (env) PS D:\Ejemplo_Streamlit> streamlit run ./Home.py
# Si hay problemas al conectar al entorno desde VSCode: en PowerShell
#   Get-ExecutionPolicy
#   Set-ExecutionPolicy Unrestricted
#   Get-ExecutionPolicy
# También puede usar: 
# Actualizar el archivo de librerías:
# pip freeze > '.\requirements.txt'
#  
# Local URL: http://localhost:8501
# Network URL: http://192.168.1.15:8501
# https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
# ico = [":anchor:", ":dart:", ":bow_and_arrow:", ":gem:", ":dizzy:", ":chart_with_upwards_trend:", ":arrows_counterclockwise:", 
#        ":zap:", ":dart:", ":dart:",  ]

# Configurar la página principal
st.set_page_config(
    page_title="SMEC",
    page_icon=":anchor:",
    initial_sidebar_state="auto",
    layout="centered"
)

# Llamar el menú
util.generarMenu()

# Crea el título
st.title("SMEC - Síndrome Metabólico de Enfermedad Cardiovascular")

# Crea el texto
st.write("""
Determinar si un paciente al cual se le realizan diferentes estudios clínicos para hallar enfermedades como: Hipertensión, Hiperglusemia, Colesterol HDL bajo, Hipertriglidicemia, Trastorno de cintura-altura y poliúrea. Además, se le preguntan datos como: Edad, Género, si fuma y si consume licor.

Todo esto con la finalidad de diagnosticar si la persona posee un síndrome metabólico asociado a enfermedad cardiovascular (SMEC), a la cual llamaremos enferdedad, una variable categórica que vamos a predecir a través del modelo de Bosques Aleatorios (Random Forest).

Los datos se encuentran en la carpeta:\n\n https://drive.google.com/drive/folders/1_E-q91yPR_wAi__1blntpTC3kXEpBHIb?usp=sharing
"""
         )

# Insertar una imagen a nuestra página
from PIL import Image
imagen = Image.open('media/Image2.jpg')
# Incrustar la imagen
st.image(imagen, caption="Enfermedad Cardiovascular",
         use_container_width=600)

# Subtitulo despues de la imagen
st.header("Key Performance Indicators (KPIs)")

# Texto después del subtítulo
st.write("""
- KPI: Identificar a través de los parámetros de las enfermedades de base de cada paciente, y sus datos médicos generales como el género, la edad, si consume o no, tabaco y alcohol, para determinar si el paciente puede padecer SMEC.
""")

#
hide_streamlit_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        </style>
        """
# Esconde los tres puntos de la derecha
st.markdown(hide_streamlit_style, unsafe_allow_html=True)



