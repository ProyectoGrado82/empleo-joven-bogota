
import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Empleo Joven Bogotá", layout="centered")

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

usuarios = []
postulaciones = []

vacantes = [
{"id": 1, "empresa": "TechBogotá", "titulo": "Desarrollador Junior", "ubicacion": "Bogotá", "habilidades": ["Python", "Trabajo en equipo"]},
{"id": 2, "empresa": "InnovaSoft", "titulo": "Asistente de Soporte Técnico", "ubicacion": "Bogotá", "habilidades": ["Comunicación", "Resolución de problemas"]},
{"id": 3, "empresa": "EcoData", "titulo": "Analista de Datos en Formación", "ubicacion": "Remoto", "habilidades": ["Excel", "Power BI", "Python"]},
{"id": 4, "empresa": "Datacy", "titulo": "Practicante de análisis de datos", "ubicacion": "Bogotá", "habilidades": ["Excel", "Python", "SQL"]},
{"id": 5, "empresa": "RedFox Digital", "titulo": "Asistente de marketing digital", "ubicacion": "Bogotá", "habilidades": ["Redes sociales", "Canva", "Google Ads"]},
{"id": 6, "empresa": "Talento TI", "titulo": "Tester de software junior", "ubicacion": "Remoto", "habilidades": ["Pruebas manuales", "Metodologías ágiles"]},
{"id": 7, "empresa": "Ecotienda App", "titulo": "Diseñador UI/UX en formación", "ubicacion": "Remoto", "habilidades": ["Figma", "Creatividad", "UX Writing"]},
{"id": 8, "empresa": "SoftGroup SAS", "titulo": "Soporte técnico nivel 1", "ubicacion": "Bogotá", "habilidades": ["Atención al cliente", "Redes", "Ticketing"]},
{"id": 9, "empresa": "Nubeco", "titulo": "Asistente de desarrollo front-end", "ubicacion": "Bogotá", "habilidades": ["HTML", "CSS", "JavaScript"]},
{"id": 10, "empresa": "EduNet", "titulo": "Auxiliar administrativo", "ubicacion": "Bogotá", "habilidades": ["Excel", "Atención telefónica"]},
{"id": 11, "empresa": "CívicaLab", "titulo": "Asistente de proyectos sociales", "ubicacion": "Bogotá", "habilidades": ["Trabajo comunitario", "Organización"]},
{"id": 12, "empresa": "TuringCode", "titulo": "Desarrollador móvil en formación", "ubicacion": "Remoto", "habilidades": ["Flutter", "Firebase"]},
{"id": 13, "empresa": "Innobrand", "titulo": "Diseñador gráfico junior", "ubicacion": "Bogotá", "habilidades": ["Photoshop", "Illustrator", "Creatividad"]},
{"id": 14, "empresa": "MediaConnect", "titulo": "Community Manager Junior", "ubicacion": "Bogotá", "habilidades": ["Redes sociales", "Comunicación", "Canva"]},
{"id": 15, "empresa": "NextSoft", "titulo": "Desarrollador Backend Jr", "ubicacion": "Remoto", "habilidades": ["Node.js", "MongoDB", "Git"]},
{"id": 16, "empresa": "SaludYa", "titulo": "Asistente administrativo en salud", "ubicacion": "Bogotá", "habilidades": ["Atención al cliente", "Excel", "Facturación"]},
{"id": 17, "empresa": "CodeHouse", "titulo": "Frontend Intern", "ubicacion": "Remoto", "habilidades": ["React", "HTML", "CSS"]},
{"id": 18, "empresa": "LogisticsPro", "titulo": "Auxiliar de bodega", "ubicacion": "Bogotá", "habilidades": ["Organización", "Trabajo físico", "Inventario"]},
{"id": 19, "empresa": "LegalSoft", "titulo": "Digitador de documentos legales", "ubicacion": "Bogotá", "habilidades": ["Digitación", "Ortografía", "Office"]},
{"id": 20, "empresa": "Financiera Plus", "titulo": "Auxiliar contable junior", "ubicacion": "Bogotá", "habilidades": ["Contabilidad básica", "Excel", "Normas NIIF"]},
{"id": 21, "empresa": "AgroTIC", "titulo": "Técnico en soporte de campo", "ubicacion": "Zona rural Cundinamarca", "habilidades": ["GPS", "Instalación de sensores", "Movilidad"]},
{"id": 22, "empresa": "RedDocentes", "titulo": "Monitor académico virtual", "ubicacion": "Remoto", "habilidades": ["Tutorías", "Didáctica", "Manejo de plataformas"]},
{"id": 23, "empresa": "BioInnova", "titulo": "Asistente de laboratorio", "ubicacion": "Bogotá", "habilidades": ["Manejo de muestras", "Normas de bioseguridad"]},
{"id": 24, "empresa": "GreenTech", "titulo": "Asistente de proyectos ambientales", "ubicacion": "Bogotá", "habilidades": ["Excel", "Trabajo en campo", "Reportes"]},
{"id": 25, "empresa": "AlphaTrans", "titulo": "Coordinador logístico junior", "ubicacion": "Bogotá", "habilidades": ["Logística", "Rutas", "ERP"]},
{"id": 26, "empresa": "DataInsight", "titulo": "Junior Data Analyst", "ubicacion": "Remoto", "habilidades": ["Python", "Pandas", "Excel"]},
{"id": 27, "empresa": "CineBogotá", "titulo": "Auxiliar de sala", "ubicacion": "Bogotá", "habilidades": ["Atención al cliente", "Ventas", "Trabajo en equipo"]},
{"id": 28, "empresa": "DocuScan", "titulo": "Escáner de documentos", "ubicacion": "Bogotá", "habilidades": ["Digitación", "Organización", "Office"]},
{"id": 29, "empresa": "AprendeYA", "titulo": "Tutor virtual de matemáticas", "ubicacion": "Remoto", "habilidades": ["Matemáticas", "Comunicación", "Didáctica"]},
{"id": 30, "empresa": "Televoz", "titulo": "Agente call center bilingüe", "ubicacion": "Bogotá", "habilidades": ["Inglés", "Atención al cliente"]},
{"id": 31, "empresa": "Artextil", "titulo": "Operario de confección", "ubicacion": "Bogotá", "habilidades": ["Costura", "Manejo de máquinas"]},
{"id": 32, "empresa": "ByteWeb", "titulo": "Diseñador web trainee", "ubicacion": "Remoto", "habilidades": ["HTML", "CSS", "Diseño responsive"]},
{"id": 33, "empresa": "CulturArte", "titulo": "Gestor cultural auxiliar", "ubicacion": "Bogotá", "habilidades": ["Organización de eventos", "Gestión cultural"]},
{"id": 34, "empresa": "MarketExpress", "titulo": "Repartidor urbano", "ubicacion": "Bogotá", "habilidades": ["Moto", "Conocimiento de direcciones"]},
{"id": 35, "empresa": "Superlimpio S.A.", "titulo": "Auxiliar de aseo", "ubicacion": "Bogotá", "habilidades": ["Limpieza", "Orden", "Puntualidad"]},
{"id": 36, "empresa": "Tienda D1", "titulo": "Vendedor tienda a tienda", "ubicacion": "Bogotá", "habilidades": ["Ventas", "Servicio al cliente"]},
{"id": 37, "empresa": "TaxiYa", "titulo": "Conductor de taxi", "ubicacion": "Bogotá", "habilidades": ["Licencia C1 o C2", "GPS", "Servicio"]},
{"id": 38, "empresa": "LogiBodega", "titulo": "Auxiliar de bodega", "ubicacion": "Bogotá", "habilidades": ["Carga", "Inventario", "Trabajo físico"]}
]

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
        st.error("❌ Por favor completa todos los campos obligatorios.")
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

        st.subheader("🎯 Vacantes recomendadas")
        compatibles = [v for v in vacantes if set(habilidades).intersection(v["habilidades"])]

        if compatibles:
            for vac in compatibles:
                with st.expander(f"{vac['titulo']} en {vac['empresa']} ({vac['ubicacion']})"):
                    st.markdown(f"- **Habilidades requeridas:** {', '.join(vac['habilidades'])}")
                    if st.button(f"✅ Postular a {vac['titulo']} ({vac['empresa']})", key=vac["id"]):
                        postulaciones.append({
                            "usuario_id": usuario["id"],
                            "vacante_id": vac["id"],
                            "fecha_postulacion": datetime.now().isoformat()
                        })
                        st.success(f"📨 Te postulaste a **{vac['titulo']}**. Te contactaremos al número `{celular}`.")
        else:
            st.warning("⚠️ No se encontraron vacantes compatibles con tu perfil.")
