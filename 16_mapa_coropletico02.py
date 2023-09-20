import pandas as pd
import folium

# Cargar los datos y preparar el DataFrame
df = pd.read_csv(r'D:\Germán\Desktop\Python Files\migration.csv')
df = df.dropna(axis=0)
df['Value'] = df['Value'].astype(int)

arg_esp = df[(df['Country of birth/nationality'] == 'Argentina') & (df['Country'] == 'Spain')]
arg_esp = arg_esp.groupby('Year')['Value'].sum().reset_index()

arg_ita = df[(df['Country of birth/nationality'] == 'Argentina') & (df['Country'] == 'Italy')]
arg_ita = arg_ita.groupby('Year')['Value'].sum().reset_index()

arg_usa = df[(df['Country of birth/nationality'] == 'Argentina') & (df['Country'] == 'United States')]
arg_usa = arg_usa.groupby('Year')['Value'].sum().reset_index()

# Preparar datos para el gráfico
categorias = ['Spain', 'Italy', 'United States of America']
valores = [arg_esp['Value'].sum(), arg_ita['Value'].sum(), arg_usa['Value'].sum()]
mapdata = {'categorias': categorias, 'valores': valores}
dfdata = pd.DataFrame(mapdata)

# Cargamos el GeoJSON mundial a la variable world_geo
import json
world_geo = json.load(open('world_countries.json', 'r', encoding='utf-8'))

# Creamos un mapa mundial:
world_map = folium.Map(location=[0, 0], zoom_start=2) # Creamos un mapa mundial

# Generamos el mapa coroplético:
world_map.choropleth(
    geo_data=world_geo,
    data=dfdata,
    columns=['categorias', 'valores'],
    key_on='feature.properties.name',
    fill_color='YlOrRd',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Emigración Argentina a España, Italia y Estados Unidos'
)

# Guarda el mapa como un archivo HTML
world_map.save('mapa_coropletico.html')

# Para verlo desde la consola de Python
import os
os.system('start mapa_coropletico.html')
