import streamlit as st
import random

# Título de la aplicación
st.title('Color War Bingo Loco')

# Definir los números del bingo
bingo_numbers = list(range(1, 131))

# Función para generar un número aleatorio


def draw_number():
    return random.choice(bingo_numbers)


# Encabezado y explicación del juego
st.header("Instructions")
st.write(
    "This is a fun bingo game for Color War! The game will randomly draw numbers between 1 and 130. "
    "You can use this app to call out numbers for your bingo game during the event."
)

# Botones para iniciar y detener el sorteo de números
if st.button('Draw Number'):
    number = draw_number()
    bingo_numbers.remove(number)  # Eliminar el número sorteado de la lista
    st.write(f"The drawn number is: **{number}**")

# Botón para resetear el juego
if st.button('Reset Game'):
    bingo_numbers[:] = list(range(1, 131))  # Restaurar la lista original
    st.write("Game reset. Ready to start again!")

# Personalización de los botones con CSS
st.markdown(
    """
    <style>
    .stButton>button {
        background-color: #ff4747;
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 20px;
        box-shadow: 0px 4px 6px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #ff6363;
    }
    </style>
    """,
    unsafe_allow_html=True
)
