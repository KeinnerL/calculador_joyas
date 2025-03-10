import json
from modules.utils.screenControlers import *
from modules.agregar.diamante import *
from modules.agregar.esmeralda  import *
from modules.agregar.zafiro  import *

#estos 3 bloques de codigo sirven para comprobar si el ID del diamante, zafiro o esmeralda ya existe 
def id_existe(biblioteca, id_buscar):
    for diamante in biblioteca["diamante"]:
        if diamante["id"] == id_buscar:
            return True
    return False

def id_existe(biblioteca, id_buscar):
    for zafiro in biblioteca["zafiro"]:
        if zafiro["id"] == id_buscar:
            return True
    return False

def id_existe(biblioteca, id_buscar):
    for esmeralda in biblioteca["esmeralda"]:
        if esmeralda["id"] == id_buscar:
            return True
    return False

#funcion para ingresar a los menus de agregar las piedras selccioandas respectivamente
def agregarJoya(ruta):
        with open (ruta,"r",encoding="utf-8") as file:
            biblioteca=json.load(file)
            try:
                casoAgregar=int(input("->"))
            except ValueError:
                print("por favor ingrese un valor valido")
                pausar_pantalla()
            match casoAgregar:
                case 1:
                    borrar_pantalla()
                    agregarDiamante()
                case 2:
                    borrar_pantalla()
                    agregarEsmeralda()
                case 3:
                    borrar_pantalla()
                    agregarZafiro()
                case 4:
                    pass