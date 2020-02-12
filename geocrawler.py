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
        except Exception:
            print('unknown error encountered: ',filepath)

try:
    # vystup ve foramtu geojson, features rozdeleny podle geometrie
    gj_structure_points = {'type': 'FeatureCollection', 'features': mypoints}
    with open("points.geojson", "w", encoding="utf-8") as p:
        json.dump(gj_structure_points, p, indent=2, ensure_ascii=False)

    gj_structure_lines = {'type': 'FeatureCollection', 'features': mylinestrings}
    with open("lines.geojson", "w", encoding="utf-8") as l:
        json.dump(gj_structure_lines, l, indent=2, ensure_ascii=False)

    gj_structure_polygons = {'type': 'FeatureCollection', 'features': mypolygons}
    with open("polygons.geojson", "w", encoding="utf-8") as po:
        json.dump(gj_structure_polygons, po, indent=2, ensure_ascii=False)

#osetreni vyjimek
except PermissionError:
    print('you do not have write permissions for: ', sys.argv[1])
except Exception:
    print('NO OUTPUT - unknown error')
