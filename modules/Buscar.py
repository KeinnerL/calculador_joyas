from modules.ui import *
from modules.utils.screenControlers import *
import json

#opción para buscar la joya de acuerdo al ID
def buscar_joya(ruta):
    with open(ruta, "r", encoding="utf-8") as file:
        biblioteca = json.load(file)  #cargar archivo JSON
    borrar_pantalla()
    print(MENU_BUSCAR)
    try:
        seleccion = int(input("Seleccione la opción que deseas realizar\n-> "))
    except ValueError:
        print("Apreciado Usuario, Usted se encuentra ingresando un caracter erróneo")
        pausar_pantalla()
        return buscar_joya(ruta)
    match seleccion:  #hacer casos de selección para poder acceder al menú de búsqueda por ID
        case 1:
            try:
                id_a_buscar = int(input("Ingrese el ID de la joya que desea buscar\n-> "))  #ingresar el ID a buscar
            except ValueError:
                print("Por favor, ingrese un número válido como ID")
                pausar_pantalla()
                return buscar_joya(ruta)
            encontrado = False  #variable para rastrear si encontramos el ID
            for categoria, piedras in biblioteca.items():
                for piedra in piedras:
                    if piedra.get("id") == id_a_buscar:  #si el ID coincide, se muestra la joya
                        print("Joya encontrada:")
                        print(json.dumps(piedra, indent=4))  #imprime la joya con formato
                        pausar_pantalla()
                        encontrado = True
                        break  #salir del bucle interno una vez encontrada la joya
                if encontrado:
                    break  #salir del bucle externo si ya se encontró
            if not encontrado:
                print("El ID no se encontró.")
                pausar_pantalla()
            return buscar_joya(ruta)  #vuelve al menú de búsqueda
        case 2:  #salir
            pausar_pantalla()
            pass
        case _:  #volver a mostrar el menú en caso de que ingrese una opción incorrecta
            return buscar_joya(ruta)
