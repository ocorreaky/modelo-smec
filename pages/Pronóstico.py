import streamlit as st
import pandas as pd
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, mean_squared_error, r2_score, confusion_matrix, ConfusionMatrixDisplay
import utilidades as util
from pickle import dump
from pickle import load
import numpy as np

# Configurar la página
st.set_page_config(
    page_title="SMEC",
    page_icon=":anchor:",
    initial_sidebar_state="auto",
    layout="centered"
)

# Llamar el menú
util.generarMenu()

#Título
st.title('SMEC - Síndrome Metabólico de Enfermedad Cardiovascular')
#subtítulo
st.header('Datos')
#leo los datos
df = pd.read_csv('data/Datos_Pacientes.csv', index_col=0)
st.markdown('** Datos de los pacientes **')
st.write(df)

# Mostrar el modelo 
st.markdown('** Resultado del modelo Random Forest para los datos históricos **')
util.modelo_rf(df)

# Generar objetos necesarios para ingresar datos
with st.sidebar:
    st.header('Datos para el Diagnóstico')
    hipertension = st.checkbox('Hipertensión')
    hiperglucemia = st.checkbox('Hiperglucemia')
    hdl = st.checkbox('HDL Bajo')
    hipertri = st.checkbox('Hipertridiglicemia')
    ica = st.checkbox('ICA')
    edad = st.number_input('Edad', min_value=18, max_value=100)
    genero = st.selectbox('Genero', ('Femenino', 'Masculino'))
    tabaco = st.checkbox('Fuma')
    alcohol = st.checkbox('Alcohol')
    poliu = st.checkbox('Poliúrea')
    btn_ejecutar = st.button('Diagnosticar')

# Lógica de la predicción
lista = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

if btn_ejecutar == True:
    if hipertension == True:
        lista[0] = 1
    else:
        lista[0] = 0
    if hiperglucemia == True:
        lista[1] = 1
    else:
        lista[1] = 0
    if hdl == True:
        lista[2] = 1
    else:
        lista[2] = 0
    if hipertri == True:
        lista[3] = 1
    else:
        lista[3] = 0
    if ica == True:
        lista[4] = 1
    else:
        lista[4] = 0
    lista[5] = edad
    
    if genero == 'Masculino':
        lista[6] = 1
    else:
        lista[6] = 0
    if tabaco == True:
        lista[7] = 1
    else:
        lista[7] = 0
    if alcohol == True:
        lista[8] = 1
    else:
        lista[8] = 0
    if poliu == True:
        lista[9] = 1
    else:
        lista[9] = 0
    
    arr = np.array([lista])
    #st.write(arr)
    
    util.prueba_modelo(arr)
