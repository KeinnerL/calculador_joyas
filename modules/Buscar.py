from modules.imports import *

def buscar_joya(ruta, id_buscar):
    with open (ruta,"r",encoding="utf-8") as file:
        biblioteca = json.load(file)
    
    borrar_pantalla()
    print(menu_buscar)
    try:
        seleccion = int(input('Seleccione la opcion que deseas realizar'))
    except ValueError:
        print('Apreciado Usuario, Usted se encuentra ingresando un caracter erroneo')
        pausar_pantalla()
        return(buscar_joya)
    else:
        match seleccion:
            case 1:
                try:
                    id_a_buscar = int(input('Ingrese el ID de la joya que desea buscar: '))
                    elemento = buscar_joya(file, id_a_buscar)
                    
                    if elemento:
                        print('Elemento encontrado:', elemento)
                    else:
                        print('No se encontro ningun elemento con ese ID')
                except ValueError:
                    print('Por favor, Ingrese un numero valido como ID')
                
                resultado = next((item for item in biblioteca if item["id"] == id_buscar),None)
                return resultado
            case 2:
                pass
