import streamlit as st

# sidebar
def sideb_config():
    st.set_page_config(
        initial_sidebar_state="collapsed",
        layout="wide",
        page_icon="🌍"
    )   

def controle_sideb():
    with st.sidebar:
        st.sidebar.header("Controle de Camadas e Mapa Base")
        st.sidebar.text_input("Pesquisar", key="pesquisa_sidebar")

        with st.expander("Mapa Base", expanded=False):
            mapa_selecionado = st.radio(
                "Selecione o Mapa Base:",
                ("Satelite", "OpenStreetMap", "Dark", "Esri World Topographic", "World Terrain Base"),
                index=0
            )

        with st.expander("Camadas", expanded=False):
            "Selecione uma Camada:",
            Setor_rotulo = st.toggle("Setor Rótulo", value=False)
            Setor_rotulo_legenda = st.toggle("Setor Rótulo Legenda", value=False)
            
    return mapa_selecionado, Setor_rotulo, Setor_rotulo_legenda