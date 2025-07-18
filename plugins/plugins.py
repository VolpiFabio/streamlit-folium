from folium.plugins import Draw, MousePosition, MeasureControl
import folium

##################### ferramenta de desenho no mapa ###################
def plugins_mapa(mapa):
    Draw(
        position="topright",
    ).add_to(mapa)

    # Fullscreen
    folium.plugins.Fullscreen(
        position="bottomright",
        title="Tela Cheia",
        title_cancel="Sair modo tela cheia",
    ).add_to(mapa)

# Mostrar Latitude e Longitude
# folium.LatLngPopup().add_to(mapa)

################ posição do mouse retorna lat, long #############

    MousePosition(position="topleft", separator=" | ", prefix="coordenadas: ").add_to(mapa)
    
    ################ medidor de distancias #############

    MeasureControl(primary_length_unit="meters").add_to(mapa)