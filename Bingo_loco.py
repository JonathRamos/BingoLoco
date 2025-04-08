import streamlit as st
import random

# Configuración de la página
st.set_page_config(
    page_title="ILC Color War Bingo Loco 2025", layout="centered")

# Título
st.markdown("<h1 style='text-align: center; color: #003366;'>ILC COLOR WAR BINGO LOCO 2025</h1>",
            unsafe_allow_html=True)

# Inicializar el estado de la sesión
if 'called_numbers' not in st.session_state:
    st.session_state.called_numbers = []
if 'last_number' not in st.session_state:
    st.session_state.last_number = None

# Mostrar el número sorteado
st.markdown("---")
if st.session_state.last_number is not None:
    st.markdown(
        f"<h2 style='text-align: center; font-size: 150px; color: #FF3333;'>🎯 {st.session_state.last_number}</h2>", unsafe_allow_html=True)
else:
    st.markdown("<h3 style='text-align: center; color: gray;'>No number called yet</h3>",
                unsafe_allow_html=True)

# Mostrar los números sorteados
st.markdown("### Numbers Called:")
called = sorted(st.session_state.called_numbers)
if called:
    st.markdown(
        f"<div style='text-align: center;'>{', '.join(str(num) for num in called)}</div>", unsafe_allow_html=True)
else:
    st.markdown("<div style='text-align: center;'>None yet</div>",
                unsafe_allow_html=True)

# Botones al final
col1, col2 = st.columns(2)

with col1:
    if st.button("🎲 Call Next Number"):
        remaining = list(set(range(1, 131)) -
                         set(st.session_state.called_numbers))
        if remaining:
            new_number = random.choice(remaining)
            st.session_state.called_numbers.append(new_number)
            st.session_state.last_number = new_number
        else:
            st.warning("All numbers have been called!")

with col2:
    if st.button("🔁 Reset Game"):
        st.session_state.called_numbers = []
        st.session_state.last_number = None
