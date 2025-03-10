import json
from modules.utils.screenControlers import *
RUTA=("./data/joyas.json")

#a traves de esta funcion podemos mirar el menu, y escoger nuestra id a eliminar
def eliminarJoya(RUTA):
        borrar_pantalla()
        print("Eliminar Joya")
        optionDelete = input("¿Deseas revisar la lista de joyas?\n1.si\n2.no\n3.salir\n-> ")
        if optionDelete == "1":
                with open(RUTA, "r", encoding="utf-8") as file:
                        biblioteca = json.load(file)
                borrar_pantalla()
                print(json.dumps(biblioteca, indent=4, ensure_ascii=False)) #esto muestra el menu 
                pausar_pantalla()
                borrar_pantalla()
                return eliminarJoya(RUTA)  #vuelve a escoger la opcion de eliminar
        elif optionDelete == '2':
                #ingresar ID de la joya
                id_joya = input("Ingrese el ID de la joya que desea eliminar:\n-> ")
                with open(RUTA, "r", encoding="utf-8") as file:
                        data = json.load(file)
                #buscar la joya dentro del JSON
                encontrada = False
                for key, joyas in data.items():
                        for joya in joyas:
                                if str(joya.get("id")) == id_joya:
                                        joyas.remove(joya)
                                        encontrada = True
                                        break  #sale del loop interno después de encontrar y eliminar
                if encontrada:
                        print(f"La joya con ID {id_joya} ha sido eliminada con éxito.")
                else:
                        print(f"El ID {id_joya} no fue encontrado.")
                # Guardar los datos actualizados
                with open(RUTA, "w", encoding="utf-8") as file:
                        json.dump(data, file, indent=4, ensure_ascii=False)
                pausar_pantalla()
                borrar_pantalla()
                return eliminarJoya(RUTA)  #volver a ejecutar la función si se desea eliminar otra joya
        elif optionDelete == '3':
                pass
        else:
                pass