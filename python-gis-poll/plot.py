import geopandas
import matplotlib.pyplot as plt
import sys
import requests
from pprint import pprint

base_path="./Taipei-shp/shape/"
natural= geopandas.read_file(base_path+"natural.shp")
landuse= geopandas.read_file(base_path+"landuse.shp")
buildings = geopandas.read_file(base_path+"buildings.shp")
roads = geopandas.read_file(base_path+"roads.shp")
railways= geopandas.read_file(base_path+"railways.shp")
waterways= geopandas.read_file(base_path+"waterways.shp")
fig, ax = plt.subplots()
natural.plot(color='green',ax=ax)
landuse.plot(color='gray',ax=ax)
buildings.plot(color='black',ax=ax)
roads.plot(color='orange',linewidth=0.3,ax=ax)
railways.plot(color='yellow',linewidth=0.6,ax=ax)
waterways.plot(color='blue',linewidth=0.3,ax=ax)

poll=requests.get("https://opendata.epa.gov.tw/api/v1/AQI?%24skip=0&%24top=1000&%24format=json").json()

pprint(poll)

plt.show()