import json,os
from pathlib import path

mypoints=[]
mylinestrings=[]
mypolygons=[]

for filepath in path(sys.argv[1]).rglob('**/*.geojson'):
    filename=os.path.basename(filepath)
    with open(filename, "r", encoding="utf-8") as f:
        fjutrs = json.load(f)


    for pod in fjutrs['features']:
        if pod['geometry']['type']=='Point':
            pod['filepath']=os.path.abspath('fjutrs')
            mypoints.append(pod)
        elif pod['geometry']['type']=='Linestring':
            pod['filepath'] = os.path.abspath('fjutrs')
            mylinestrings.append(pod)
        elif pod['geometry']['type']=='Polygon':
            pod['filepath'] = os.path.abspath('fjutrs')
            mypolygons.append(pod)
        else:
            pass


with open("points.geojson","w",encoding="utf-8") as p:
    json.dump(mypoints,p,indent=2,ensure_ascii=False)

with open("linestrings.geojson","w",encoding="utf-8") as l:
    json.dump(mylinestrings,l,indent=2,ensure_ascii=False)

with open("polygons.geojson","w",encoding="utf-8") as po:
    json.dump(mypolygons,po,indent=2,ensure_ascii=False)