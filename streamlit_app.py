import streamlit as st

st.title("👕 Mi Colección de Camisetas")
st.subheader("Bienvenido a mi aplicación")

# Un pequeño mensaje
st.write("Esta es una lista de mis camisetas:")

# Una lista interactiva
camisetas = ["España - Euro 2024", "Argentina - Messi", "Real Madrid - Vintage"]
seleccion = st.selectbox("¿Cuál es tu favorita?", camisetas)

st.info(f"Has elegido la de: {seleccion}")
