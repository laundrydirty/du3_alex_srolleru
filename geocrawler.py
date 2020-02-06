#import pouzitych funkci
import json,sys
from pathlib import Path

#vytvoreni prazdnych feature seznamu podle geometrie
mypoints=[]
mylinestrings=[]
mypolygons=[]

#hledane pripony
extensions=['*.geojson','*.json']
for e in extensions:
    #funkce najde soubory s hledanymi priponami v adresari zadanem v prikazove radce
    for filepath in Path(sys.argv[1]).rglob(e):
        try:
            #vstup dat
            with open(filepath, "r", encoding="utf-8") as f:
                try:
                    features = json.load(f)
                    #informuje o tom jaky soubor zpracovava
                    print(filepath)
                    for feat in features['features']:
                        #deleni podle geometrie
                        if feat['geometry']['type'] == 'Point':
                            #zapis cesty k souboru
                            feat['properties']['filepath'] = str(filepath)
                            #ulozeni do prislusneho seznamu
                            mypoints.append(feat)
                        elif feat['geometry']['type'] == 'LineString':
                            feat['properties']['filepath'] = str(filepath)
                            mylinestrings.append(feat)
                        elif feat['geometry']['type'] == 'Polygon':
                            feat['properties']['filepath'] = str(filepath)
                            mypolygons.append(feat)
                        else:
                            pass
                #osetreni vyjimek
                except json.JSONDecodeError:
                    print('invalid JSON format: ', filepath)
        except PermissionError:
            print('you do not have permission to open file: ', filepath)

#vystup ve foramtu geojson, features rozdeleny podle geometrie
with open("points.geojson","w",encoding="utf-8") as p:
    json.dump(mypoints,p,indent=2,ensure_ascii=False)

with open("lines.geojson","w",encoding="utf-8") as l:
    json.dump(mylinestrings,l,indent=2,ensure_ascii=False)

with open("polygons.geojson","w",encoding="utf-8") as po:
    json.dump(mypolygons,po,indent=2,ensure_ascii=False)
