import streamlit as st
import os

# Configurar título de la página y diseño
st.set_page_config(page_title="Portafolio de Julio", layout="wide")

# ----------- BIENVENIDA -----------

# Agregar estilos con HTML para los títulos
st.markdown("""
    <style>
    .titulo-principal {
        font-size: 48px;
        color: #1E90FF;
        text-align: center;
        font-weight: bold;
        margin-top: 30px;
        margin-bottom: 10px;
    }
    .subtitulo {
        font-size: 24px;
        color: #666666;
        text-align: center;
        margin-bottom: 40px;
    }
    </style>
""", unsafe_allow_html=True)

# Título y subtítulo en HTML
st.markdown("""
    <div class="titulo-principal">👋 Hola, soy Julio André Ríos Cuba</div>
    <div class="subtitulo">Estudiante de Comunicación Audiovisual</div>
""", unsafe_allow_html=True)

# Introducción breve
st.write("Bienvenido a mi portafolio. Aquí comparto algunos de mis trabajos y procesos creativos.")

# ----------- SOBRE MÍ -----------

st.markdown("---")
st.markdown("<h2 style='color:#1E90FF;'>🧑 Sobre mí</h2>", unsafe_allow_html=True)

# Texto descriptivo
st.markdown("""
<p style='font-size:18px; text-align:justify;'>
Soy Julio André Ríos Cuba, nací y crecí en Cusco. Por motivos de estudios me mudé a Lima en el año 2022, para estudiar la carrera de comunicación audiovisual en la Pontificia Universidad Católica del Perú. Soy un gran aficionado del basket, tanto de jugarlo como de verlo. Me encanta el trap argentino (Sobre todo Duki y Khea).
</p>
""", unsafe_allow_html=True)

# Mostrar 4 fotos personales en fila
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.image("files/foto_julio_1.jpg", use_container_width=True)
with col2:
    st.image("files/foto_julio_2.jpg", caption="Reflejo", use_container_width=True)
with col3:
    st.image("files/foto_julio_3.jpg", caption="Exteriores", use_container_width=True)
with col4:
    st.image("files/foto_julio_4.jpg", caption="Blanco y negro", use_container_width=True)

# ----------- CAPACIDADES Y VIRTUDES -----------

st.markdown("---")
st.markdown("<h2 style='color:#1E90FF;'>💡 Capacidades y virtudes</h2>", unsafe_allow_html=True)

# Lista de virtudes y habilidades
st.markdown("""
- 🎨 Creatividad para proponer soluciones visuales únicas.
- 🗣️ Buena comunicación y trabajo en equipo.
- 🎬 Experiencia en fotografía y producción audiovisual.
- 📚 Interés constante por aprender y mejorar.
- 🤝 Empatía y compromiso con causas sociales.
""")

# ----------- CONTACTO -----------

st.markdown("---")
st.markdown("<h2 style='color:#1E90FF;'>📫 Contacto</h2>", unsafe_allow_html=True)

# Datos de contacto y redes sociales
st.markdown("""
Si deseas ponerte en contacto conmigo para colaboraciones, proyectos o simplemente conversar sobre audiovisual, puedes escribirme a:

- ✉️ **julio.rios@example.com**  
- 📷 [Instagram](https://instagram.com/julio_foto)  
- 🔗 [LinkedIn](https://linkedin.com/in/juliorios)  
""", unsafe_allow_html=True)

# ----------- EXPERIENCIA -----------

st.markdown("---")
st.markdown("<h2 style='color:#1E90FF;'>💼 Experiencia</h2>", unsafe_allow_html=True)

# Experiencias profesionales y educativas
st.markdown("""
- 📸 **Community Manager y fotógrafo** en *Éxodo Family Basketball Club* (2023 - actualidad)  
- 📷 **Creación de contenido** para la *Liga Mixta Deportiva de Basketball de Saylla - Cusco* (2022)  
- 🎓 **Estudios universitarios** en *Pontificia Universidad Católica del Perú* - Comunicación Audiovisual (2022 - actualidad)  
- 🏫 **Educación escolar** en *Colegio La Merced - Cusco*  
""")

# ----------- PROYECTOS -----------

st.markdown("---")
st.markdown("<h2 style='color:#1E90FF;'>🎬 Mis proyectos</h2>", unsafe_allow_html=True)

# Texto destacado en celeste
st.markdown("""
<p style='font-size:20px; color:#00BFFF; text-align:center;'>  🎥 Aquí podras encontrar algunos videos y fotos que realice como parte de mi experiencia pre y profesional.    </p>
""", unsafe_allow_html=True)

# Botón para mostrar/ocultar proyectos
if "ver_proyectos" not in st.session_state:
    st.session_state.ver_proyectos = False

if st.button("📂 Ver proyectos"):
    st.session_state.ver_proyectos = not st.session_state.ver_proyectos

if st.session_state.ver_proyectos:

    # -------- CLUB ÉXODO --------
    st.markdown("### 🏀 Club Éxodo")
    st.markdown("Trabajé como fotógrafo para: Exodo Family Basquetball Club.")

    # VIDEOS de Club Éxodo
    st.markdown("#### 🎥 Videos")
    descripciones = {
        1: "Video de reconocimiento del jugador Fabio Ríos como seleccionado del equipo de Saylla Cusco (2023).",
        2: "Video de resumen de partido del club Exodo en contra del Club Titanes (2022).",
        3: "Video promocional para el ciclo de verano 2025 del club Éxodo."
    }

    for i in range(1, 4):
        video_path = f"files/video_exodo_{i}.mp4"
        if os.path.exists(video_path):
            # Mostrar video si el archivo existe
            st.video(video_path)
            # Mostrar descripción personalizada debajo del video
            st.markdown(f"<p style='color:gray;'>{descripciones[i]}</p>", unsafe_allow_html=True)
        else:
            # Mostrar advertencia si no se encuentra el video
            st.warning(f"⚠️ No se encontró el archivo: {video_path}")

    # FOTOS de Club Éxodo
    st.markdown("#### 📸 Galería fotográfica – Club Éxodo")
    # Iterar en bloques de 4 fotos para mostrarlas en filas de 4 columnas
    for row in range(0, 24, 4):
        cols = st.columns(4)
        for i in range(4):
            idx = row + i + 1  # Índice de la foto actual
            if idx <= 24:
                img_path = f"files/foto_exodo_{idx}.jpg"  # Ruta dinámica
                if os.path.exists(img_path):
                    with cols[i]:
                        # Mostrar imagen si existe
                        st.image(img_path, use_container_width=True, caption=f"Foto {idx}")
                else:
                    with cols[i]:
                        # Advertencia si falta la imagen
                        st.warning(f"Falta foto_exodo_{idx}.jpg")

    # -------- PROYECTOS PERSONALES --------
    st.markdown("### 🎞️ Proyectos personales")
    st.markdown("Exploraciones visuales sobre emociones, ciudad e intimidad.")

    # FOTOS de proyectos personales
    st.markdown("#### 📸 Galería fotográfica – Proyectos personales")
    # Iterar en bloques de 3 fotos para mostrarlas en filas de 3 columnas
    for row in range(0, 12, 3):
        cols = st.columns(3)
        for i in range(3):
            idx = row + i + 1  # Índice de la foto actual
            if idx <= 12:
                img_path = f"files/foto_proyecto_{idx}.jpg"  # Ruta dinámica
                if os.path.exists(img_path):
                    with cols[i]:
                        # Mostrar imagen si existe
                        st.image(img_path, use_container_width=True, caption=f"Proyecto {idx}")
                else:
                    with cols[i]:
                        # Advertencia si falta la imagen
                        st.warning(f"Falta foto_proyecto_{idx}.jpg")