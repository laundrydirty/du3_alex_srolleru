import json,sys
from pathlib import Path

mypoints=[]
mylinestrings=[]
mypolygons=[]

extensions=['*.geojson','*.json']
for e in extensions:
    for filepath in Path(sys.argv[1]).rglob(e):
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                try:
                    fjutrs = json.load(f)
                    print(filepath)
                    for pod in fjutrs['features']:
                        if pod['geometry']['type'] == 'Point':
                            pod['filepath'] = str(filepath)
                            mypoints.append(pod)
                        elif pod['geometry']['type'] == 'LineString':
                            pod['filepath'] = str(filepath)
                            mylinestrings.append(pod)
                        elif pod['geometry']['type'] == 'Polygon':
                            pod['filepath'] = str(filepath)
                            mypolygons.append(pod)
                        else:
                            pass
                except json.JSONDecodeError:
                    print('invalid JSON format: ', filepath)
        except PermissionError:
            print('invalid JSON format: ', filepath)


with open("points.geojson","w",encoding="utf-8") as p:
    json.dump(mypoints,p,indent=2,ensure_ascii=False)

with open("lines.geojson","w",encoding="utf-8") as l:
    json.dump(mylinestrings,l,indent=2,ensure_ascii=False)

with open("polygons.geojson","w",encoding="utf-8") as po:
    json.dump(mypolygons,po,indent=2,ensure_ascii=False)