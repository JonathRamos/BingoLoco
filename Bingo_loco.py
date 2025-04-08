import streamlit as st
import random
from PIL import Image

# Configuración de la página
st.set_page_config(page_title="Color War Bingo Loco", layout="centered")


# Título
st.markdown("<h1 style='text-align: center; color: #FF5733;'>Color War Bingo Loco</h1>",
            unsafe_allow_html=True)

# Generar número aleatorio
if 'number' not in st.session_state:
    st.session_state.number = random.randint(1, 130)

# Mostrar número en grande
st.markdown(
    f"<h1 style='text-align: center; font-size: 100px; color: #3498db;'>{st.session_state.number}</h1>", unsafe_allow_html=True)

# Botón para generar nuevo número
if st.button('Get New Number', key='new_number', help="Generates a random number for bingo!", style="background-color: #FF5733; color: white; padding: 10px 20px; font-size: 20px;"):
    st.session_state.number = random.randint(1, 130)
    st.experimental_rerun()

# Botón para reiniciar el número
if st.button('Reset Number', key='reset', help="Resets the number to a random value", style="background-color: #2ecc71; color: white; padding: 10px 20px; font-size: 20px;"):
    st.session_state.number = random.randint(1, 130)
    st.experimental_rerun()
