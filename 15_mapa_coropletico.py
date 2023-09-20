import pandas as pd
import folium

# Creamos un Dataframe con los datos migratorios de Canadá
df_can = pd.read_excel('Canada.xlsx', sheet_name='Canada by Citizenship', skiprows=range(20), skipfooter=2)

# Limpiamos el Dataframe
df_can.drop(['AREA','REG','DEV','Type','Coverage'], axis=1, inplace=True) # Eliminamos columnas innecesarias
df_can.rename(columns={'OdName':'Country', 'AreaName':'Continent','RegName':'Region'}, inplace=True) # Renombramos algunas columnas
df_can.columns = list(map(str, df_can.columns)) # Convertimos a string todos los nombres de las columnas
df_can['Total'] = df_can.sum(axis=1) #Agregamos una columna de totales

# Cargamos el GeoJSON mundial a la variable world_geo
import json
world_geo = json.load(open('world_countries.json', 'r', encoding='utf-8'))

###CREAMOS EL MAPA COROPLETICO###
# Creamos un mapa mundial:
world_map = folium.Map(location=[0, 0], zoom_start=2) # Creamos un mapa mundial

# Generamos el mapa coroplético de la inmigración total de cada país a Canadá de 1980 a 2013
world_map.choropleth(                   # Aplicamos el método choropleth() al mapa mundial que creamos (y completamos sus parámetros)
    geo_data=world_geo,                 # GeoJSON file
    data=df_can,                        # Dataframe con los datos migratorios de Canadá
    columns=['Country', 'Total'],       # Columnas del Dataframe que se usarán para crear el mapa coroplético
    key_on='feature.properties.name',   # La key o variable en el archivo GeoJSON que contiene el nombre de la variable que nos interesa
    fill_color='YlOrRd',                # Paleta de colores
    fill_opacity=0.7,                   # Transparencia del relleno
    line_opacity=0.2,                   # Tansparencia de las líneas
    legend_name='Inmigración a Canada'  # Título
)

# Guarda el mapa como un archivo HTML
world_map.save('mapa_coropletico_inmigracion_Canada.html')

# Para verlo desde la consola de Python
import os
os.system('start mapa_coropletico_inmigracion_Canada.html')
