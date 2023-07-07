import folium
import webbrowser


azores = folium.Map(location=(38, -27), zoom_start=6)
azores.save("mapa.html")

# Otwarcie pliku HTML w przeglądarce
webbrowser.open("mapa.html")

print(folium.__all__)
print(folium.__file__)

