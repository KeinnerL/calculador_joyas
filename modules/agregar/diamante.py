import json
from modules.utils.screenControlers import *
from modules.ui import *

#funcion de agregar diamantes
def agregarDiamante():
    def id_existe(biblioteca, id_buscar):
        for diamante in biblioteca["diamante"]:
            if diamante["id"] == id_buscar:
                return True
    with open ("./data/joyas.json","r",encoding="utf-8") as file: #carga el archivo con ruta joyas.json
            biblioteca=json.load(file)
    borrar_pantalla()
    print(MENU_QUILATE_DIAMANTE) #todas estas constantes son los menus invocados para cada caso 
    try:
        casoC=int(input("->"))
        match casoC:
            case 1: #parametros 
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
    print(MENU_CALIDAD_CORTE_DIAMANTE)
    try:
        casoCr=int(input("->"))
        match casoCr:
            case 1:
                corte=1.20
            case 2:
                corte=1.10 #parametros
            case 3:
                corte=1.00
            case 4:
                corte=0.90
            case 5:
                corte=0.80
            case _:
                corte=1.20
                print("La eleccion ingresada no existe....")
                pausar_pantalla()
    except ValueError:
        print("Por favor ingrese una eleccion valida...")
        pausar_pantalla()
    borrar_pantalla()
    print(MENU_COLOR_DIAMANTE)
    try:
        casoCL=int(input("->"))
        match casoCL:
            case 1:
                color="d-f"
            case 2:
                color="g-j"
            case 3:# parametros 
                color="k-m"
            case 4:
                color="n-z"
            case 5:
                color="fan"
            case _:
                color='d-f'
                print("La eleccion ingresada no existe....")
                pausar_pantalla()
    except ValueError:
        print("Por favor ingrese una eleccion valida...")
        pausar_pantalla()
    borrar_pantalla()
    print(MENU_CLARIDAD_DIAMANTE)
    try:
            casoCLA=int(input("->"))
            match casoCLA:
                case 1:
                    claridad=1.50
                case 2:
                    claridad=1.30
                case 3:
                    claridad=1.15
                case 4:
                    claridad=1.00 #parametros 
                case 5:
                    claridad=0.75
                case _:
                    claridad=1.50
                    print("La eleccion ingresada no existe....")
                    pausar_pantalla()
    except ValueError:
            print("Por favor ingrese una eleccion valida...")
            pausar_pantalla()
    borrar_pantalla()
    print(MENU_CANTIDAD_DIAMANTES)
    try:
            cantidadDiamantes=int(input("->"))
    except ValueError:
            print("Por favor ingrese una eleccion valida...")
            pausar_pantalla()    
    borrar_pantalla()
    print(MENU_METAL_DIAMANTES)
        
    try:
        casoMT=int(input("->"))
        match casoMT:
            case 1:
                metal="oro"
            case 2: #parametros
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
    print(MENU_GRAMAJE_DIAMANTES)
    try:
        gramaje=float(input("->"))
    except ValueError:
        print("Por favor ingrese una eleccion valida...")
        pausar_pantalla()
    #0.50 quilates
    if quilate==0.50 and color=="d-f":
        precioBQ1=5000
        precioBQ2=9000
    elif quilate==0.50 and color=="g-j":
        precioBQ1=4000
        precioBQ2=7000
    elif quilate==0.50 and color=="k-m":
        precioBQ1=2500
        precioBQ2=5000 #parametros
    elif quilate==0.50 and color=="n-z":
        precioBQ1=1500
        precioBQ2=3500
    elif quilate==0.50 and color=="fan":
        precioBQ1=8000
        precioBQ2=50000
    #1.00 quilates
    elif quilate==1.00 and color=="d-f":
        precioBQ1=8000
        precioBQ2=16000
    elif quilate==1.00 and color=="g-j":
        precioBQ1=6500
        precioBQ2=13000
    elif quilate==1.00 and color=="k-m":
        precioBQ1=4000
        precioBQ2=8000
    elif quilate==1.00 and color=="n-z":
        precioBQ1=2500
        precioBQ2=6000
    elif quilate==1.00 and color=="fan":
        precioBQ1=15000
        precioBQ2=100000
    #1.50 quilates
    elif quilate==1.50 and color=="d-f":
        precioBQ1=10000
        precioBQ2=22000
    elif quilate==1.50 and color=="g-j":
        precioBQ1=8500
        precioBQ2=17000
    elif quilate==1.50 and color=="k-m":
        precioBQ1=5500
        precioBQ2=11000
    elif quilate==1.50 and color=="n-z":
        precioBQ1=3500
        precioBQ2=8000
    elif quilate==1.50 and color=="fan":
        precioBQ1=25000
        precioBQ2=250000
    #2.00
    elif quilate==2.00 and color=="d-f":
        precioBQ1=14000
        precioBQ2=35000
    elif quilate==2.00 and color=="g-j":
        precioBQ1=11000
        precioBQ2=25000
    elif quilate==2.00 and color=="k-m":
        precioBQ1=7000
        precioBQ2=16000
    elif quilate==2.00 and color=="n-z":
        precioBQ1=5000
        precioBQ2=12000
    elif quilate==2.00 and color=="fan":
        precioBQ1=50000
        precioBQ2=1000000
    if metal=="oro":
        valormetal=93.65*gramaje
    elif metal=="plata" :
        valormetal=1.05*gramaje
    elif metal=="no tiene":
        valormetal=0
        #agarra todos los parametros que se pidieron previamente con el fin de calcular un 
        #valor minimo y un maximo, es por ello que a lo largo del codigo se veian tantas variables y casos
    valorfinalmin=(((precioBQ1*(quilate**1.5)*corte*claridad)*cantidadDiamantes)+valormetal) 
    valorfinalmax=(((precioBQ2*(quilate**1.5)*corte*claridad)*cantidadDiamantes)+valormetal)
    while True:
        try:
            borrar_pantalla()
            #pide el ID y en caso de que sea existente, avisa al usuario
            id = int(input("Por favor ingrese un ID  único:\n->")) 
            if id_existe(biblioteca, id):
                print(" Error: El ID ya existe. Intente con otro.")
            else:
                break  
        except ValueError:
            print("Por favor ingrese un ID válido (solo números).")
    #forma u estructura con la cual se va a crear el JSON 
    dicDiamante={"id":id,
                "quilate":quilate,
                "corte":corte,
                "color":color,
                "cantidad":cantidadDiamantes,
                "metal":metal,
                "valorMin":int(valorfinalmin),
                "valorMax":int(valorfinalmax)}
    biblioteca["diamante"].append(dicDiamante)
    with open ("./data/joyas.json","w") as k2:
        json.dump(biblioteca,k2,indent=4) #añade los valores al JSON 
        borrar_pantalla()
        print("Diamante agregado con exito.")
        pausar_pantalla()

#toda esta documentación aplica para el documento "esmeraldas.py" y "zafiro.py"