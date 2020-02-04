#du3
import json
from pathlib import Path


with open("input.geojson","r",encoding="utf-8") as f:
    fjutrs=json.load(f)

mypoints=[]
mylinestrings=[]
mypolygons=[]

for pod in fjutrs['features']:
    if pod['geometry']['type']=='Point':
        pod['filepath']=pathlib(fjutrs)
        mypoints.append(pod)
    elif pod['geometry']['type']=='Linestring':

        mylinestrings.append(pod)
    elif pod['geometry']['type']=='Polygon':

        mypolygons.append(pod)
    else:
        print(chyba)


with open("points.geojson","w",encoding="utf-8") as f:
    json.dump(mypoints,f,indent=2,ensure_ascii=False)

with open("linestrings.geojson","w",encoding="utf-8") as f:
    json.dump(mylinestrings,f,indent=2,ensure_ascii=False)

with open("polygons.geojson","w",encoding="utf-8") as f:
    json.dump(mypolygons,f,indent=2,ensure_ascii=False)