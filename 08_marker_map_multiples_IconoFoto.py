import folium

# Crea un objeto de mapa centrado en una ubicación inicial
m = folium.Map(location=[51.5074, -0.1278], zoom_start=10)  # Latitud y longitud de Londres

# Datos de los marcadores (ubicación, texto emergente y ruta de la imagen personalizada)
marcadores = [
    {
        'location': [51.5074, -0.1278],  # Latitud y longitud de Londres
        'popup': 'Londres',
        'image_path': 'london.jpg'  # Ruta de la imagen personalizada para Londres
    },
    {
        'location': [40.7128, -74.0060],  # Latitud y longitud de Nueva York
        'popup': 'Nueva York',
        'image_path': 'newyork.jpg'  # Ruta de la imagen personalizada para Nueva York
    },
    {
        'location': [34.0522, -118.2437],  # Latitud y longitud de Los Ángeles
        'popup': 'Los Ángeles',
        'image_path': 'losangeles.jpg'  # Ruta de la imagen personalizada para Los Ángeles
    }
]

# Agrega los marcadores al mapa con imágenes personalizadas
for marcador in marcadores:
    folium.Marker(
        location=marcador['location'],
        popup=folium.Popup(marcador['popup'], max_width=300),  # Popup personalizado
        icon=folium.CustomIcon(icon_image=marcador['image_path'], icon_size=(50, 50))  # Ícono personalizado con imagen
    ).add_to(m)

# Guarda el mapa en un archivo HTML
m.save("mapa_con_marcadores_imagenes.html")

# Para verlo desde la consola de Python
import os
os.system('start mapa_con_marcadores_imagenes.html')
