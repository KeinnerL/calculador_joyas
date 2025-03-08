import json

def ver_json(ruta):
    with open(ruta, "r", encoding="utf-8") as joyas:
        data = json.load(joyas)
    print(data)