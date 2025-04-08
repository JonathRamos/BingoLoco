import streamlit as st
import random

# Título de la aplicación
st.title('ILC COLOR WAR BINGO LOCO 2025')

# Definir los números del bingo
bingo_numbers = list(range(1, 131))
drawn_numbers = []

# Función para generar un número aleatorio


def draw_number():
    return random.choice(bingo_numbers)

# Función para actualizar los números ya sorteados


def update_drawn_number(number):
    drawn_numbers.append(number)
    bingo_numbers.remove(number)


# Mostrar el número sorteado
st.markdown(
    """
    <style>
    .number-box {
        background-color: white;
        color: red;
        font-size: 150px;
        font-weight: bold;
        text-align: center;
        padding: 20px;
        border-radius: 10px;
        width: 400px;
        margin: 0 auto;
        box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
    }
    .stButton>button {
        background-color: #ff4747;
        color: white;
        border-radius: 50%;
        padding: 20px 40px;
        font-size: 20px;
        box-shadow: 0px 4px 6px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
        width: 150px;
        height: 150px;
    }
    .stButton>button:hover {
        background-color: #ff6363;
    }
    .numbers-list {
        font-size: 20px;
        color: black;
        margin-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Generar número cuando el botón es presionado
if st.button('Draw Number'):
    if bingo_numbers:  # Verificar que aún haya números disponibles
        number = draw_number()
        update_drawn_number(number)
        st.markdown(
            f'<div class="number-box">{number}</div>', unsafe_allow_html=True)
    else:
        st.write("No more numbers left to draw!")

# Mostrar lista de números ya sorteados
if drawn_numbers:
    st.markdown("<h3>Drawn Numbers:</h3>", unsafe_allow_html=True)
    for num in drawn_numbers:
        st.write(num)

# Botón para resetear el juego
if st.button('Reset Game'):
    bingo_numbers[:] = list(range(1, 131))  # Restaurar la lista original
    drawn_numbers.clear()  # Limpiar la lista de números sorteados
    st.write("Game reset. Ready to start again!")
