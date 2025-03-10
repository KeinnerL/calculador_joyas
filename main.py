from modules.imports import *

RUTA=("./data/joyas.json")
crearJson(RUTA)

#a traves de esta funcion se puede ingresar a las funciones principales que ofrece el programa
def menu():
    #aca se le limpia la pantalla al usario y se abre el menu principal 
    borrar_pantalla()
    print(MENU_INICIO)
    try: #se hace validacion con el fin de evitar datos erroneos que no corresponden al menu principal
        opcion_menu = int(input('Seleccione la opcion que deseas realizar:\n-> '))
    except ValueError:
        print('Apreciado Usuario, Usted se encuentra ingresando un caracter erroneo')
        pausar_pantalla()
        return menu()
    else:
        match opcion_menu: #se invoca la funcion que seleccione el usuario y su menu correspondiente
            case 1:
                borrar_pantalla()
                print(MENU_AGREGAR)
                agregarJoya(RUTA)
                return menu()
            case 2:
                borrar_pantalla()
                ver_json(RUTA)
                pausar_pantalla()
                return menu()
            case 3:
                borrar_pantalla()
                print(MENU_EDITAR)
                try:
                    accionEditar=int(input("-> "))
                    match accionEditar:
                        case 1:
                            borrar_pantalla()
                            eliminarJoya(RUTA)
                            return menu()
                        case 2:
                            return menu()
                        case _:
                            return menu()
                except ValueError:
                    print("por favor ingrese una opcion valida")
            case 4:
                borrar_pantalla()
                print(MENU_BUSCAR)
                buscar_joya(RUTA)
                return menu()
            case 5:
                pass
            case _: #este caso sirve en caso de que el usuario no ignrese un valor correspondiente pero pueda seguir usando el programa
                print('usuario, usted ingreso un valor de menu no correspondiente')
                pausar_pantalla()
                return menu()

#bajo esta condicion se invoca el menu en caso de que el nombre del archivo sea "main"
if __name__ == "__main__":
    menu()