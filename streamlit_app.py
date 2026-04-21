import streamlit as st

st.title("👕 Mi Colección de Camisetas")
st.subheader("Bienvenido a mi app de fútbol")

# Un pequeño mensaje
st.write("Esta es una lista de mis camisetas favoritas:")

# Una lista interactiva
camisetas = ["España - Euro 2024", "Argentina - Messi", "Real Madrid - Vintage", "Japan - Special Edition"]
seleccion = st.selectbox("¿Cuál es tu favorita?", camisetas)

st.info(f"Has elegido la de: {seleccion}")
