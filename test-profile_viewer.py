import streamlit as st
from beem import Hive
from beem.account import Account
import json

# Conectar a un nodo de hive
h = Hive(node=["https://api.hive.blog"])

st.write("Visor de perfiles de hive")

def info_cuenta(username):
    #crear una instancia de la clase Account
    cuenta = Account(username, blockchain_instance=h)

    #obtener la metadata de la cuenta
    perfil_cuenta = json.loads(cuenta["posting_json_metadata"])

    #Obtener la foto de perfil de la cuenta
    foto_cuenta = perfil_cuenta["profile"]["profile_image"]

    info_cuenta("joheredia21")

    return cuenta, perfil_cuenta, foto_cuenta

col1, col2 = st.columns([3, 1])
col3, col4 = st.columns([1, 3])

with col1:
    #obtener info de la cuenta
    username = st.text_input(" ")#"ingrese el nombre de la cuenta")

with col2:
    st.markdown("<br>", unsafe_allow_html=True)
    busqueda_boton = st.button(label="Buscar", type='primary', use_container_width=True)

#activar la funcion cuando se hace click

if busqueda_boton and username:
    
    #obtener info de la cuenta
    cuenta, perfil_cuenta, foto_cuenta = info_cuenta(username)

    #mostrar foto
    st.image(foto_cuenta, width=500)

    st.write(cuenta)


    with col3:
        #Mostrar informacion de la cuenta
        st.write(f'Nombre : {cuenta['name']}')

    with col4:
        #mostrar la MEMO KEY de la cuenta
        st.write(f"MEMO KEY: {cuenta['memo_key']}")