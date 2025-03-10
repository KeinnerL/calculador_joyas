import json
from tabulate import tabulate
from modules.utils.screenControlers import *

def ver_json(ruta):
    #abrir y cargar el JSON
    with open(ruta, "r", encoding="utf-8") as joyas:
        data = json.load(joyas)
    #crear una lista para la tabla
    tabla = []
    #recorrer el diccionario y resetear los datos de acuerdo a la cantidad de datos que haya para definir el bucle
    for key, lista in data.items():
        if lista: #en caso de que haya datos en la lista
            for joya in lista:
                tabla.append([
                    key, joya.get("id", "N/A"), joya.get("quilate", "N/A"), 
                    joya.get("corte", "N/A"), joya.get("color", "N/A"), 
                    joya.get("cantidad", "N/A"), joya.get("metal", "N/A"), 
                    joya.get("valorMin", "N/A"), joya.get("valorMax", "N/A")
                ])
        else:  #en caso de que la lista está vacía, mostrar "no hay datos"
            tabla.append([key, "no hay datos", "-", "-", "-", "-", "-", "-", "-"])
    #se definen los encabezados de la tabla
    headers = ["Joya", "ID", "Quilate", "Corte", "Color", "cantidad", "metal", "valor Minimo", "valor Maximo"]
    print(tabulate(tabla, headers=headers, tablefmt="fancy_grid"))