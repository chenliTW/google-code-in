import geopandas
import matplotlib.pyplot as plt
import sys

folder=str(sys.argv[1])
base_path="./{}shape/".format(folder)
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
plt.show()