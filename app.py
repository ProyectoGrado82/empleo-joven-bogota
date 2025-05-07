
import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Empleo Joven Bogotá", layout="centered")

# --- Bienvenida ---
st.markdown("""
# 👋 Bienvenido a **Empleo Joven Bogotá**

🎯 *Transformación Digital del Empleo Juvenil: Una Herramienta Móvil para Bogotá*

Desarrollado por estudiantes de Ingeniería de Sistemas de la UNAD.

Este prototipo busca facilitar la inclusión laboral formal de jóvenes entre 18 y 28 años en Bogotá, conectándolos con vacantes que se ajusten a sus habilidades.

Una iniciativa académica impulsada por:
- Johan Manuel Santana Cortes
- Edison Fernando Cardenas Bermudez
- Danis Daniel Peniche Ospino

👨‍🏫 Tutor: Daniel Andrés Guzmán Arévalo  
📚 Escuela de Ciencias Básicas, Tecnología e Ingeniería – UNAD  
📅 Abril de 2025
""", unsafe_allow_html=True)

st.divider()
st.subheader("🧾 Registro de usuario")

# Datos globales
usuarios = []
postulaciones = []

# Vacantes mínimas de prueba (puedes pegar todas después)
vacantes = [
    {"id": 1, "empresa": "TechBogotá", "titulo": "Desarrollador Junior", "ubicacion": "Bogotá", "habilidades": ["Python", "Trabajo en equipo"]},
    {"id": 2, "empresa": "InnovaSoft", "titulo": "Soporte Técnico", "ubicacion": "Bogotá", "habilidades": ["Comunicación", "Resolución de problemas"]},
    {"id": 3, "empresa": "MarketExpress", "titulo": "Repartidor", "ubicacion": "Bogotá", "habilidades": ["Moto", "Conocimiento de direcciones"]},
]

# Habilidades
habilidades_unicas = sorted({h for v in vacantes for h in v["habilidades"]})

with st.form("registro"):
    nombre = st.text_input("👤 Nombre completo")
    correo = st.text_input("📧 Correo electrónico")
    celular = st.text_input("📱 Número de celular")
    ciudad = st.text_input("📍 Ciudad")
    formacion = st.text_input("🎓 Formación académica")
    habilidades = st.multiselect("💼 Habilidades", habilidades_unicas)
    submit = st.form_submit_button("🔎 Buscar vacantes compatibles")

if submit:
    if not nombre or not correo or not celular:
        st.error("Por favor completa todos los campos obligatorios.")
    else:
        usuario = {
            "id": len(usuarios) + 1,
            "nombre": nombre,
            "correo": correo,
            "celular": celular,
            "ciudad": ciudad,
            "formacion": formacion,
            "habilidades": habilidades,
            "fecha_registro": datetime.now().isoformat()
        }
        usuarios.append(usuario)
        st.success(f"✅ Usuario registrado: {nombre}")

        # Mostrar vacantes compatibles
        st.subheader("🎯 Vacantes recomendadas")
        compatibles = [v for v in vacantes if set(habilidades).intersection(v["habilidades"])]

        if compatibles:
            for vac in compatibles:
                with st.expander(f"{vac['titulo']} en {vac['empresa']} ({vac['ubicacion']})"):
                    st.markdown(f"- **Requisitos:** {', '.join(vac['habilidades'])}")
                    if st.button(f"✅ Postular a {vac['titulo']} ({vac['empresa']})", key=vac["id"]):
                        postulaciones.append({
                            "usuario_id": usuario["id"],
                            "vacante_id": vac["id"],
                            "fecha_postulacion": datetime.now().isoformat()
                        })
                        st.success(f"📨 Te postulaste a {vac['titulo']} - te contactaremos al {celular}.")
        else:
            st.warning("⚠️ No se encontraron vacantes compatibles.")
