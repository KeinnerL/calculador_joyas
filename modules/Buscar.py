from modules.ui import *
from modules.utils.screenControlers import *
import json

def buscar_joya(ruta):
    with open (ruta,"r",encoding="utf-8") as file:
        biblioteca = json.load(file)
    
    borrar_pantalla()
    print(menu_buscar)
    try:
        seleccion = int(input('Seleccione la opcion que deseas realizar'))
    except ValueError:
        print('Apreciado Usuario, Usted se encuentra ingresando un caracter erroneo')
        pausar_pantalla()
        return buscar_joya(ruta)
    else:
        match seleccion:
            case 1:
                try:
                    id_a_buscar = int(input('Ingrese el ID de la joya que desea buscar: '))
                except ValueError:
                    print('Por favor, Ingrese un numero valido como ID')
                    return buscar_joya(ruta)    
                    
                for categorias, piedras in biblioteca.items():
                    for piedra in piedras:
                        if piedra.get("id")==id_a_buscar:
                            print(piedra)
                        else:
                            print("el id no se encontro.")
                return buscar_joya(ruta)
            case 2:
                pass
            case _:
                return buscar_joya(ruta)
