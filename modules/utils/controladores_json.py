import json

#funcion para la creacion del json en caso de que no este creado
def crearJson(ruta):
    try:
        with open (ruta,"r") as file:
            json.load(file)
            print("archivo abierto.")
    except FileNotFoundError :
        with open (ruta,"w",encoding="utf-8") as file:
            dic={"diamante":[],
                "esmeralda":[],
                "zafiro":[]}
            json.dump(dic,file)
            print("archivo creado.")
