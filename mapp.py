#Name: Neil Felix
#Date: 10/17
#Info:

import folium
import pandas as pd


cuny = pd.read_csv('cunyLocations.csv')
#print (cuny["Campus"])

mapCUNY = folium.Map([40.768731, -73.964915])
#folium.Marker([40.77, -73.97], popup = 'Hunter').add_to(mp)

for index,row in cuny.iterrows():
    lat = row["Latitude"]
    lon = row["Longitude"]
    name = row["Campus"]
    newMarker = folium.Marker([lat, lon], popup=name)
    newMarker.add_to(mapCUNY)

mapCUNY.save(outfile = 'cuny.html')
