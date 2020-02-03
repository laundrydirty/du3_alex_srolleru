#du3
import json
from pathlib import Path


with open("input.geojson","r",encoding="utf-8") as f:
    fjutrs=json.load(f)

mypoints=[]
mylinestrings=[]
mypolygons=[]

if fjutrs['features']['geometry']['type']=='Point':
    fjutrs['features']['properties']['filepath']=pathlib(fjutrs)
    mypoints.append()
elif fjutrs['features']['geometry']['type']=='Linestring':

    mylinestrings.append()
elif fjutrs['features']['geometry']['type']=='Polygon':

    mypolygons.append()
else:
    print(chyba)


with open("points.geojson","w",encoding="utf-8") as f:
    json.dump(mypoints,f,indent=2,ensure_ascii=False)

with open("linestrings.geojson","w",encoding="utf-8") as f:
    json.dump(mylinestrings,f,indent=2,ensure_ascii=False)

with open("polygons.geojson","w",encoding="utf-8") as f:
    json.dump(mypolygons,f,indent=2,ensure_ascii=False)