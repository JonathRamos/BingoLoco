import streamlit as st
import random

st.set_page_config(page_title="Color War Bingo Loco", layout="centered")

# Title
st.markdown("<h1 style='text-align: center; color: #003366;'>🎉 Color War Bingo Loco 🎉</h1>",
            unsafe_allow_html=True)

# Initialize session state
if 'called_numbers' not in st.session_state:
    st.session_state.called_numbers = []
if 'last_number' not in st.session_state:
    st.session_state.last_number = None

# Buttons
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

# Display last number
st.markdown("---")
if st.session_state.last_number is not None:
    st.markdown(
        f"<h2 style='text-align: center; font-size: 60px; color: #FF3333;'>🎯 {st.session_state.last_number}</h2>", unsafe_allow_html=True)
else:
    st.markdown("<h3 style='text-align: center; color: gray;'>No number called yet</h3>",
                unsafe_allow_html=True)

# Show called numbers
st.markdown("### Numbers Called:")
called = sorted(st.session_state.called_numbers)
if called:
    st.markdown(
        f"<div style='text-align: center;'>{', '.join(str(num) for num in called)}</div>", unsafe_allow_html=True)
else:
    st.markdown("<div style='text-align: center;'>None yet</div>",
                unsafe_allow_html=True)
