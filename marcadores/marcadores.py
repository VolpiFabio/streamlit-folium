import folium
import pandas as pd

# Exemplo de marcadores no mapa
def marcadores_mapa(mapa):
    folium.Marker(
        [-22.645830, -47.196110], 
        popup="Cosmópolis", 
        tooltip="Centro",
        icon=folium.Icon(icon="info-sign", color="blue")
    ).add_to(mapa)
    folium.Marker(
        [-22.625409932556146, -47.186705815182904],
        popup="Comercio",
        tooltip="Mercado",
        icon=folium.Icon(icon="shop", prefix="fa"),
    ).add_to(mapa)
    folium.Marker(
        [-22.635935057941218, -47.1891894106097],
        popup="Residencial",
        tooltip="Residencia",
        icon=folium.Icon(icon="home"),
    ).add_to(mapa)
    