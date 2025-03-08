from modules.imports import *

def buscar_joya():
    borrar_pantalla()
    print(menu_buscar)
    try:
        seleccion = input('Seleccione la opcion que deseas realizar')
    except ValueError:
        print('Apreciado Usuario, Usted se encuentra ingresando un caracter erroneo')
        pausar_pantalla()
        return(buscar_joya)
    else:
        match seleccion:
            case 1:
                pass
            case 2:
                pass