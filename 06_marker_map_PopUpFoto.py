import folium

# Crea un objeto de mapa centrado en una ubicación inicial
m = folium.Map(location=[51.5074, -0.1278], zoom_start=10)  # Latitud y longitud de Londres

# Define el contenido personalizado del popup como una cadena HTML
popup_content = """
    <h1>Londres</h1>
    <p>La capital del Reino Unido</p>
    <img src="london.jpg" alt="Imagen de Londres" width="200">
"""

# Crea un marcador con un popup personalizado
folium.Marker(
    location=[51.5074, -0.1278],
    popup=folium.Popup(popup_content, max_width=300)  # Utiliza Popup para contenido personalizado
).add_to(m)

# Guarda el mapa en un archivo HTML
m.save("mapa_con_popup_personalizado.html")

# Para verlo desde la consola de Python
import os
os.system('mapa_con_popup_personalizado.html')
