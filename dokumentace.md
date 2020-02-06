# Sběr dat v adresářové struktuře 

Program `geocrawler.py` nalzene všechna geodata v adresáři a rozdělí je podle geometrie na body linie a polygony.
### Popis 
Vstupem je adresář a všechny jeho podadresáře obsahující jednotlivé soubory. Program vybere, ty ve formátu `GeoJSON` a `JSON`, se kterými bude dále pracováno. Soubory ve validním formátu jsou otevřeny a jednotlivé features jsou následně podle typu geometrie ukládány do nových seznamů, spolu s absolutní cestou k původnímu souboru. 

Spouštení probíhá z příkazové řádky. Za `py geocrawler.py` uživatel zadá absolutní cestu adresáře, který chce aby byl prohledán. Ukázkový spouštěcí příkaz: `py geocrawler.py C:\Users\asrol\PycharmProjects\untitled\du3_testdata`. Program do příkazové řádky vypisuje absolutní cestu souborů `JSON` a `GeoJSON`, které prošel. Pokud narazí na soubor, který nemůže otevřít nebo není validní, vypíše u daného souboru hlášku `invalid JSON format`.

Výstupem jsou tři souboury ve fomátu `GeoJSON`, kde jsou jednotlivé features rozděleny podle geometrie na body, linie a poygony -  `points.geojson`, `lines.geojson` a `polygons.geojson`. Zároveň každá feature obsahuje nový atribut `filepath` s cestou k původnímu souboru, odkud pochází. 
