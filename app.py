"""Portafolio de Diana Azulvide en Streamlit.

Muestra el archivo portafolio-diana-azulvide.html a pantalla completa.
Los dos archivos deben estar en la misma carpeta.

Para probarlo en tu computadora:
    pip install -r requirements.txt
    streamlit run app.py
"""
from pathlib import Path

import streamlit as st

ARCHIVO_HTML = Path(__file__).parent / "Diana Azulvide · Portafolio"

st.set_page_config(
    page_title="Diana Azulvide · Portafolio",
    page_icon="🎨",
    layout="wide",
)

# Quita la barra superior, el menú y los márgenes de Streamlit para que
# el portafolio ocupe toda la ventana, y pinta el fondo del mismo crema.
st.html(
    """
    <style>
      header[data-testid="stHeader"], #MainMenu, footer,
      [data-testid="stToolbar"], [data-testid="stDecoration"] { display: none !important; }
      .stApp { background: #fcf3ed; }
      .stMainBlockContainer, .block-container {
        padding: 0 !important;
        max-width: 100% !important;
      }
      [data-testid="stVerticalBlock"] { gap: 0 !important; }
      iframe { display: block; border: 0; }
    </style>
    """
)

if not ARCHIVO_HTML.exists():
    st.error(f"No encuentro {ARCHIVO_HTML.name}. Debe estar en la misma carpeta que app.py.")
    st.stop()

if hasattr(st, "iframe"):
    # Streamlit 1.56 o posterior: el alto se ajusta solo al contenido.
    st.iframe(ARCHIVO_HTML, height="content")
else:
    # Versiones anteriores: alto fijo con barra de desplazamiento propia.
    import streamlit.components.v1 as components

    components.html(ARCHIVO_HTML.read_text(encoding="utf-8"), height=900, scrolling=True)
