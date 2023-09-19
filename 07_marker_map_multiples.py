import folium

# Crea un objeto de mapa centrado en una ubicación específica
m = folium.Map(location=[51.5074, -0.1278], zoom_start=10)  # Latitud y longitud de Londres

# Agrega múltiples marcadores al mapa
# Marcador 1
folium.Marker(
    location=[51.5074, -0.1278],  # Latitud y longitud del marcador 1
    popup="Londres",  # Texto emergente del marcador 1
    icon=folium.Icon(icon="star")  # Ícono del marcador 1 (puedes usar otros íconos)
).add_to(m)

# Marcador 2
folium.Marker(
    location=[40.7128, -74.0060],  # Latitud y longitud del marcador 2
    popup="Nueva York",  # Texto emergente del marcador 2
    icon=folium.Icon(icon="heart")  # Ícono del marcador 2 (puedes usar otros íconos)
).add_to(m)

# Marcador 3
folium.Marker(
    location=[34.0522, -118.2437],  # Latitud y longitud del marcador 3
    popup="Los Ángeles",  # Texto emergente del marcador 3
    icon=folium.Icon(icon="info-sign")  # Ícono del marcador 3 (puedes usar otros íconos)
).add_to(m)

# Guarda el mapa como un archivo HTML
m.save('mapa01.html')

# Para verlo desde la consola de Python
import os
os.system('start mapa01.html')
