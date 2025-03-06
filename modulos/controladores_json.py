import json


def crearJson(ruta):
    try:
        with open (ruta,"r") as file:
            json.load(file)
            print("archivo abierto.")
    except FileNotFoundError :
        with open (ruta,"w",encoding="utf-8") as file:
            dic={}
            json.dump(dic,file)
            print("archivo creado.")
