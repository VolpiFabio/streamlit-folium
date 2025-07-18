import folium

# camadas
def camadas_mapa(mapa, geoserver_url, Setor_rotulo, Setor_rotulo_legenda):
    camada_setor_rotulo = "SP_Americana:setor_rotulo"
    camada_setor_rotulo_legenda = "SP_Americana:setor_rotulo_legenda"


    if Setor_rotulo:
        folium.WmsTileLayer(
            url=geoserver_url,
            layers=camada_setor_rotulo,
            fmt="image/png",
            name="Setor Rótulo",
            transparent=True,
            version="1.3.0",
            overlay=True,
            control=True,
            show=True
        ).add_to(mapa)

    if Setor_rotulo_legenda:
        folium.WmsTileLayer(
            url=geoserver_url,
            layers=camada_setor_rotulo_legenda,
            fmt="image/png",
            name="Setor Rótulo Legenda",
            transparent=True,
            version="1.3.0",
            overlay=True,
            control=True,
            show=True
        ).add_to(mapa)