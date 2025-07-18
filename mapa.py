import streamlit as st
import folium
from streamlit_folium import st_folium
from dotenv import load_dotenv
load_dotenv()

# modulos
from marcadores.marcadores import marcadores_mapa
from plugins.plugins import plugins_mapa
from sidebar.sidebar import sideb_config, controle_sideb
from mapa_base.mapa_base import mapas_base
from camadas.camadas import camadas_mapa
from url_geoserver.geo_url import geoserver_url

# sidebar
sideb_config()
mapa_selecionado, Setor_rotulo, Setor_rotulo_legenda = controle_sideb()

# inicia o mapa em um local (latitude, longitude)
local = [-22.645830, -47.196110]

# define as variaveis de zoom
default_zoom = 10
max_zoom = 19
min_zoom = 1

mapa_zoom = st.session_state.get("mapa_zoom", default_zoom)
map_center = st.session_state.get("map_center", local)
mapa_zoom = min(max(mapa_zoom, min_zoom),max_zoom)

# Cria o mapa
mapa = folium.Map(
    location=local, 
    zoom_start=mapa_zoom, 
    control_scale=True,
    max_zoom=max_zoom,
    min_zoom=min_zoom
)

# plugins
plugins_mapa(mapa)

# mapas base
mapas_base(mapa, mapa_selecionado)

# adiciona camadas

url = geoserver_url()
camadas_mapa(mapa, url, Setor_rotulo, Setor_rotulo_legenda)

# marcadores
marcadores_mapa(mapa)


# texto estilizado usando markdown com css
def info():
    st.markdown(
        f"""
        <h6 style = 'color: #B0C4DE;'>
        Abra o menu lateral (clique na seta no canto superior esquerdo) para selecionar o mapa base e as camadas."
        </h6>
    """,
        unsafe_allow_html=True
    )
info()

# Exibe o mapa no Streamlit
retorno = st_folium(mapa, width="100%", height=600)

if retorno:
    if "zoom" in retorno:
        st.session_state["mapa_zoom"] = int(retorno["zoom"])
    if "center" in retorno :
        st.session_state["map_center"] = retorno["center"]



