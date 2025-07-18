import folium

# mapa base
def mapas_base(mapa, mapa_selecionado):
    if mapa_selecionado == "OpenStreetMap":
        folium.TileLayer("OpenStreetMap", name="OpenStreetMap").add_to(mapa)

    elif mapa_selecionado == "Satelite" :
            folium.TileLayer(
        tiles="https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
                name="Satélite",
                attr="Esri World Imagery",
                overlay=True,
                control=True,
                show=True
        ).add_to(mapa)

    elif mapa_selecionado == "Dark":
            folium.TileLayer(
        tiles="https://cartodb-basemaps-{s}.global.ssl.fastly.net/dark_all/{z}/{x}/{y}.png",
            name="Dark",
            attr="CartoDB Dark Matter",
            overlay=True,
            control=True,
            show=True
        ).add_to(mapa)

    elif mapa_selecionado == "Esri World Topographic":
            folium.TileLayer(
                tiles="https://server.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer/tile/{z}/{y}/{x}",
                name='Esri World Topographic',
                attr="Esri World Topographic",
                overlay=True,
                control=True,
                show=True
        ).add_to(mapa)
    elif mapa_selecionado == "World Terrain Base":
            folium.TileLayer(
                tiles = "https://server.arcgisonline.com/ArcGIS/rest/services/World_Terrain_Base/MapServer/tile/{z}/{y}/{x}",
                name='World Terrain Base',
                attr="World Terrain Base",
                overlay=True,
                control=True,
                show=True
            ).add_to(mapa)