import json
import modules.utils.screenControlers as sc
from modules.agregar.diamante import *
def id_existe(biblioteca, id_buscar):
    for diamante in biblioteca["diamante"]:
        if diamante["id"] == id_buscar:
            return True
    return False

def agregarJoya(ruta):
        with open (ruta,"r",encoding="utf-8") as file:
            biblioteca=json.load(file)
            try:
                casoAgregar=int(input(""))
            except ValueError:
                print("por favor ingrese un valor valido")
                sc.pausar_pantalla
            
            match casoAgregar:
                case 1:
                    sc.borrar_pantalla
                    agregarDiamante()
                case 2:
                    pass
                case 3:
                    pass
                case 4:
                    pass
                case 5:
                    pass