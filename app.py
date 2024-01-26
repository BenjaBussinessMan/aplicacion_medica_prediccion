# -*- coding: utf-8 -*-
"""
streamlit app para prediccion medica
"""
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

from streamlit_extras.app_logo import add_logo

def logo():
    add_logo("logo.jpg", height=100)

logo_url = "logo.png"
st.sidebar.image(logo_url)



col1, col2, col3, col4 , col5 , col6 = st.columns([1, 40, 40,50,60,60])
with col6:
    st.write("Proyecto Final ED APP")

#modelos 

diabetes_model = pickle.load(open('modelos/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('modelos/heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open('modelos/parkinsons_model.sav', 'rb'))


st.title('Herramienta de Análisis Médico')


# Menu lateral
with st.sidebar:
    
    selected = option_menu('Selección de enfermedad',
                          
                          ['Predicción de Diabetes',
                           'Predicción de enfermedad cardíaca',
                           'Predicción de la enfermedad de Parkinson'],
                          icons=['bi-clipboard2-pulse-fill','bi-heart-pulse-fill','bi-person-standing-dress'],
                          menu_icon="cast",
                          default_index=1)

#diabetes pagina

if (selected == 'Predicción de Diabetes'):
    
    st.title('Predicción de Diabetes')
    

    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Numero de embarazos')
        
    with col2:
        Glucose = st.text_input('Nivel de glucosa')
    
    with col3:
        BloodPressure = st.text_input('Valor de presión sanguinea')
    
    with col1:
        SkinThickness = st.text_input('Valor de espesor de piel')
    
    with col2:
        Insulin = st.text_input('Nivel de insulina')
    
    with col3:
        BMI = st.text_input('Indice de masa corporal')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Valor de la función de diabetes (DPF)')
    
    with col2:
        Age = st.text_input('Edad')
    

    diab_diagnosis = ''

    
    if st.button('Resultado de prueba de diabetes'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'La persona es diabetica'
        else:
          diab_diagnosis = 'La persona no es diabetica'
        
    st.success(diab_diagnosis)




# Cardiaca pagina
if (selected == 'Predicción de enfermedad cardíaca'):
    
    st.title('Predicción de enfermedad cardíaca')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Edad')
        
    with col2:
        sex = st.text_input('Sexo')
        
    with col3:
        cp = st.text_input('Tipos de dolor en el pecho')
        
    with col1:
        trestbps = st.text_input('Presión arterial en reposo')
        
    with col2:
        chol = st.text_input('Colestoral sérico en mg/dl')
        
    with col3:
        fbs = st.text_input('Azúcar en sangre en ayunas > 120 mg/dl')
        
    with col1:
        restecg = st.text_input('Resultados electrocardiográficos en reposo')
        
    with col2:
        thalach = st.text_input('Frecuencia cardíaca máxima alcanzada')
        
    with col3:
        exang = st.text_input('Angina inducida por ejercicio')
        
    with col1:
        oldpeak = st.text_input('Depresión del ST inducida por el ejercicio.')
        
    with col2:
        slope = st.text_input('Pendiente del segmento ST del ejercicio máximo')
        
    with col3:
        ca = st.text_input('Vasos principales coloreados por fluoroscopia.')
        
    with col1:
        thal = st.text_input('tal: 0 = normal; 1 = defecto solucionado; 2 = defecto reversible')
        
        
     
    
    heart_diagnosis = ''

    
    if st.button('Resultado de enfermedad cardiaca'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'La persona tiene una enfermedad cardiaca'
        else:
          heart_diagnosis = 'La persona no tiene una enfermedad cardiaca'
        
    st.success(heart_diagnosis)
        
    
    

# Parkinson's pagina
if (selected == "Predicción de la enfermedad de Parkinson"):
    
    st.title("Predicción de la enfermedad de Parkinson")
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
        
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
        
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
        
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
        
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Absoluto)')
        
    with col1:
        RAP = st.text_input('MDVP:RAP')
        
    with col2:
        PPQ = st.text_input('MDVP:PPQ')
        
    with col3:
        DDP = st.text_input('Jitter:DDP')
        
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')
        
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
        
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')
        
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')
        
    with col3:
        APQ = st.text_input('MDVP:APQ')
        
    with col4:
        DDA = st.text_input('Shimmer:DDA')
        
    with col5:
        NHR = st.text_input('NHR')
        
    with col1:
        HNR = st.text_input('HNR')
        
    with col2:
        RPDE = st.text_input('RPDE')
        
    with col3:
        DFA = st.text_input('DFA')
        
    with col4:
        spread1 = st.text_input('spread1')
        
    with col5:
        spread2 = st.text_input('spread2')
        
    with col1:
        D2 = st.text_input('D2')
        
    with col2:
        PPE = st.text_input('PPE')
        
    parkinsons_diagnosis = ''
    
    if st.button("Resultado de la prueba de Parkinson"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "La persona tiene la enfermedad de Parkinson"
        else:
          parkinsons_diagnosis = "La persona no tiene la enfermedad de Parkinson"
        
    st.success(parkinsons_diagnosis)
