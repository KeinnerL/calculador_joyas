from os import system
import sys

#esto sirve para agregar funciones que son diferentes en los 3 sistemas operativos 
def borrar_pantalla():
    if sys.platform == "linux" or sys.platform == "darwin":
        system("clear")
    else:
        system("cls")

def pausar_pantalla():
    if sys.platform == "linux" or sys.platform == "darwin":
        x=input("Presione un tecla para continuar")
        return x
    else:
        system("pause")