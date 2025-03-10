import json
from modules.utils.screenControlers import *
from modules.ui import *

#funcion de agregar esmeralda 
def agregarEsmeralda():
    def id_existe(biblioteca, id_buscar):
        for esmeralda in biblioteca["esmeralda"]:
            if esmeralda["id"] == id_buscar:
                return True
    with open ("./data/joyas.json","r",encoding="utf-8") as file:
            biblioteca=json.load(file)
    borrar_pantalla()
    print(MENU_QUILATE_ESMERALDA)
    try:
        casoC=int(input("->"))
        match casoC:
            case 1:
                quilate=0.50
            case 2:
                quilate=1.00
            case 3:
                quilate=1.50
            case 4:
                quilate=2.00
            case _:
                quilate=0.50
                print("La eleccion ingresada no existe....")
                pausar_pantalla()
    except ValueError:
        print("Por favor ingrese una eleccion valida...")
        pausar_pantalla()
    borrar_pantalla()
    print(MENU_COLOR_ESMERALDA)
    try:
        casoCL=int(input("->"))
        match casoCL:
            case 1:
                color="Verde intenso"
            case 2:
                color="Verde medio"
            case 3:
                color="Verde claro"
            case _:
                color="Verde intenso"
                print("La eleccion ingresada no existe....")
                pausar_pantalla()
    except ValueError:
        print("Por favor ingrese una eleccion valida...")
        pausar_pantalla()
    borrar_pantalla()
    print(MENU_CLARIDAD_ESMERALDA)
    try:
            casoCLA=int(input("->"))
            match casoCLA:
                case 1:
                    claridad=1.50
                case 2:
                    claridad=1.20
                case 3:
                    claridad=1.00
                case _:
                    claridad=1.50
                    print("La eleccion ingresada no existe....")
                    pausar_pantalla()
    except ValueError:
            print("Por favor ingrese una eleccion valida...")
            pausar_pantalla()
    borrar_pantalla()
    print(MENU_CANTIDAD_ESMERALDA)
    try:
            cantidadEsmeraldas=int(input("->"))
    except ValueError:
            print("Por favor ingrese una eleccion valida...")
            pausar_pantalla()    
    borrar_pantalla()
    print(MENU_METAL_ESMERALDAS)
        
    try:
        casoMT=int(input("->"))
        match casoMT:
            case 1:
                metal="oro"
            case 2:
                metal="plata"
            case 3:
                metal="no tiene"
            case _:
                metal="oro"
                print("La eleccion ingresada no existe....")
                pausar_pantalla()
    except ValueError:
        print("Por favor ingrese una eleccion valida...")
        pausar_pantalla()
    borrar_pantalla()
    print(MENU_GRAMAJE_ESMERALDAS)
    try:
        gramaje=float(input("->"))
    except ValueError:
        print("Por favor ingrese una eleccion valida...")
        pausar_pantalla()
    #0.50 quilates
    if quilate==0.50 and color=="Verde intenso":
        precioBQ1=4000
        precioBQ2=8000
    elif quilate==0.50 and color=="Verde medio":
        precioBQ1=3000
        precioBQ2=6000
    elif quilate==0.50 and color=="Verde claro":
        precioBQ1=8500
        precioBQ2=16000
    #1.00 quilates
    elif quilate==1.00 and color=="Verde intenso":
        precioBQ1=8000
        precioBQ2=16000
    elif quilate==1.00 and color=="Verde medio":
        precioBQ1=6000
        precioBQ2=12000
    elif quilate==1.00 and color=="Verde claro":
        precioBQ1=4000
        precioBQ2=8000
    #1.50 quilates
    elif quilate==1.50 and color=="Verde intenso":
        precioBQ1=12000
        precioBQ2=24000
    elif quilate==1.50 and color=="Verde medio":
        precioBQ1=9000
        precioBQ2=18000
    elif quilate==1.50 and color=="Verde claro":
        precioBQ1=6000
        precioBQ2=12000
    #2.00
    elif quilate==2.00 and color=="Verde intenso":
        precioBQ1=20000
        precioBQ2=40000
    elif quilate==2.00 and color=="Verde medio":
        precioBQ1=15000
        precioBQ2=30000
    elif quilate==2.00 and color=="Verde claro":
        precioBQ1=10000
        precioBQ2=20000
    if metal=="oro":   
        valorMetal=93.65*gramaje
    elif metal=="plata" :
        valorMetal=1.05*gramaje
    elif metal=="no tiene":
        valorMetal=0
    valorfinalmin=(((precioBQ1*claridad)*cantidadEsmeraldas)+valorMetal)
    valorfinalmax=(((precioBQ2*claridad)*cantidadEsmeraldas)+valorMetal)
    while True:
        try:
            borrar_pantalla()
            id = int(input("Por favor ingrese un ID  único\n->"))
            if id_existe(biblioteca, id):
                print(" Error: El ID ya existe. Intente con otro.")
                pausar_pantalla()
            else:
                break  
        except ValueError:
            print("Por favor ingrese un ID válido (solo números).")
    dicEsmeralda={"id":id,
                "quilate":quilate,
                "color":color,
                "cantidad":cantidadEsmeraldas,
                "metal":metal,
                "valorMin":int(valorfinalmin),
                "valorMax":int(valorfinalmax)}
    biblioteca["esmeralda"].append(dicEsmeralda)
    with open ("./data/joyas.json","w") as k2:
        json.dump(biblioteca,k2,indent=4)
        borrar_pantalla()
        print("Esmeralda agregada con exito.")
        pausar_pantalla()