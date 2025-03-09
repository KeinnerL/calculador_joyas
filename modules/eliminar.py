import json
import utils.screenControlers as sc
RUTA=("./data/joyas.json")
sc.borrar_pantalla()
def eliminarJoya():
        sc.borrar_pantalla
        print("Eliminar Joya")
        option = input("¿Deseas revisar la lista de joyas?(s/n)\n -> ").lower()
        if option != "n":
                with open (RUTA,"r",encoding="utf-8") as file:
                        biblioteca=json.load(file)
                sc.borrar_pantalla()
                print(json.dumps(biblioteca, indent=4))
                sc.pausar_pantalla()
                sc.borrar_pantalla()
                return eliminarJoya()
        else:
                option !="s"
                id = input("Ingrese el id de la Joya\n-> ")
                with open(RUTA, "r", encoding="utf-8") as file:
                        data = json.load(file)
                if id in data:
                        del data[id]
                        print(f"El id '{id}' de la joya ha sido eliminada con éxito.")
                        sc.pausar_pantalla
                                                
                else:
                        print(f"El id '{id}' de la joya no se encuentra.")
                        with open(RUTA, "w", encoding="utf-8") as file:
                                json.dump(data, file, indent=4, ensure_ascii=False)
                        sc.pausar_pantalla()
                        sc.borrar_pantalla()
                        return eliminarJoya()

eliminarJoya()