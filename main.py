import tabulate
from modules.imports import *

RUTA=("./data/joyas.json")
crearJson(RUTA)

def menu():
    borrar_pantalla()
    print(menu_inicio)
    try:
        opcion_menu = input('Seleccione la opcion que deseas realizar')
    except ValueError:
        print('Apreciado Usuario, Usted se encuentra ingresando un caracter erroneo')
        pausar_pantalla()
        return menu()
    else:
        match opcion_menu:
            case 1:
                pass
            case 2:
                pass
            case 3:
                borrar_pantalla()
                print(menu_editar)
                try:
                    option = input('Seleccione la opcion que deseas realizar')
                except ValueError:
                    print('Apreciado Usuario, Usted se encuentra ingresando un caracter erroneo')
                    pausar_pantalla
                    return menu()
                else:
                    match option:
                        case 1:
                            pass
                        case 2:
                            pass
                        case 3:
                            print('Regresando al menu principal')
                            return menu()

