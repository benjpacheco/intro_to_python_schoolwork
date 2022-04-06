#Name:  Benyir J Pacheco
#Email: benyir.pacheco60@myhunter.cuny.edu.
#Date:  April 30, 2020

import folium
import pandas as pd

in_input = input('Enter CSV file: ')
out_input = input('Enter file save: ')
cuny = pd.read_csv(in_input)



mapCUNY = folium.Map(location=[40.768731, -73.964915])

for index,row in cuny.iterrows():
    lat = row["LATITUDE"]
    lon = row["LONGITUDE"]
    name = row["TIME"]
    newMarker = folium.Marker([lat, lon], popup=name)
    newMarker.add_to(mapCUNY)
    print(index, row)
mapCUNY.save(outfile=out_input)

