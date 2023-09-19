import folium

# Crea un objeto de mapa centrado en una ubicación específica
londres = folium.Map(location=[51.5074, -0.1278], zoom_start=10)  # Latitud y longitud de Londres

# Agrega un marcador al mapa
folium.Marker(
    location=[51.5074, -0.1278],  # Latitud y longitud del marcador
    popup='Londres',  # Texto emergente del marcador
    icon=folium.Icon(icon="fa fa-solid fa-wifi")  # Íconos de Font Awesome - https://fontawesome.com/
).add_to(londres)

# Guarda el mapa como un archivo HTML
londres.save('mapa_londres.html')

# Para verlo desde la consola de Python
import os
os.system('start mapa_londres.html')
