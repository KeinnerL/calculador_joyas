import json
import modules.utils.screenControlers as sc

def agregarDiamante():
    def id_existe(biblioteca, id_buscar):
        for diamante in biblioteca["diamante"]:
            if diamante["id"] == id_buscar:
                return True
    with open ("./data/joyas.json","r",encoding="utf-8") as file:
            biblioteca=json.load(file)
    sc.borrar_pantalla()
    print("""
=========================================
    |Quilate de el diamante|
=========================================
1.0.50 ct
2.1.00 ct
3.1.50 ct  
4.2.00 ct                  
Por favor ingrese quilate de el diamante.                         
""")
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
                print("La eleccion ingresada no existe....")
    except ValueError:
        print("Por favor ingrese una eleccion valida...")
        sc.pausar_pantalla()
    sc.borrar_pantalla()
    print("""
========================================================
|Calidad de el corte|
========================================================
Por favor ingrese la calidad del corte de el diamante.
1.Excelente
2.Muy bueno
3.Bueno
4.Regular
5.Pobre                             
""")
    try:
        casoCr=int(input("->"))
        match casoCr:
            case 1:
                corte=1.20
            case 2:
                corte=1.10
            case 3:
                corte=1.00
            case 4:
                corte=0.90
            case 5:
                corte=0.80
            case _:
                print("La eleccion ingresada no existe....")
    except ValueError:
        print("Por favor ingrese una eleccion valida...")
        sc.pausar_pantalla()
    sc.borrar_pantalla()
    print("""
==========================================
|Color|
==========================================
Por favor ingrese el color del diamante.
1.D-F (Incoloro)
2.G-J (Casi incoloro)
3.K-M (Tono ligero)
4.N-Z (Amarillo/Marrón)
5.Fantasia(Azul, Rosa, Verde, Amarillo intenso, Rojo.)                         
""")
    try:
        casoCL=int(input("->"))
        match casoCL:
            case 1:
                color="d-f"
            case 2:
                color="g-j"
            case 3:
                color="k-m"
            case 4:
                color="n-z"
            case 5:
                color="fan"
            case _:
                print("La eleccion ingresada no existe....")
    except ValueError:
        print("Por favor ingrese una eleccion valida...")
        sc.pausar_pantalla()
    sc.borrar_pantalla()
    print("""
==========================================
|Claridad|
==========================================
Por favor ingrese la claridad del diamante.
1.FL(Sin efectos)
2.VVS1-VVS2(Muy pocas inclusiones)
3.VS1-VS2 (Pequeñas inclusiones)
4.SI1-SI2 (Inclusiones visibles con lupa)
5.I1-I3 (Inclusiones visibles a simple vista)                  
""")
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
                    claridad=1.00
                case 5:
                    claridad=0.75
                case _:
                    print("La eleccion ingresada no existe....")
                    sc.pausar_pantalla()
    except ValueError:
            print("Por favor ingrese una eleccion valida...")
            sc.pausar_pantalla()
    sc.borrar_pantalla()
    print("""
==========================================
|Cantidad de diamantes|
==========================================
Ingrese la cantidad de diamantes.                 
""")
    try:
            cantidadDiamantes=int(input("->"))
    except ValueError:
            print("Por favor ingrese una eleccion valida...")
            sc.pausar_pantalla()    
    sc.borrar_pantalla()
    print("""
==========================================
|Metal|
==========================================
Por favor elija el metal de la joya.
1.Oro
2.Plata
3.No posee               
""")
        
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
                print("La eleccion ingresada no existe....")
                x=input("Presione enter para continuar.")
    except ValueError:
        print("Por favor ingrese una eleccion valida...")
        sc.pausar_pantalla()
    sc.borrar_pantalla()
    print("""
==========================================
|Gramaje metal|
==========================================
Por favor ingrese el numero de gramos de el metal.
(en caso de no tener ingrese 0).         
""")
    try:
        gramaje=float(input("->"))
    except ValueError:
        print("Por favor ingrese una eleccion valida...")
        sc.pausar_pantalla()
    #0.50 quilates
    if quilate==0.50 and color=="d-f":
        precioBQ1=5000
        precioBQ2=9000
    elif quilate==0.50 and color=="g-j":
        precioBQ1=4000
        precioBQ2=7000
    elif quilate==0.50 and color=="k-m":
        precioBQ1=2500
        precioBQ2=5000
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
    valorfinalmin=(((precioBQ1*(quilate**1.5)*corte*claridad)*cantidadDiamantes)+valormetal)
    valorfinalmax=(((precioBQ2*(quilate**1.5)*corte*claridad)*cantidadDiamantes)+valormetal)
    while True:
        try:
            sc.borrar_pantalla()
            id = int(input("Por favor ingrese un ID  único: "))
            if id_existe(biblioteca, id):
                print(" Error: El ID ya existe. Intente con otro.")
            else:
                break  
        except ValueError:
            print("Por favor ingrese un ID válido (solo números).")
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
        json.dump(biblioteca,k2,indent=4)
        sc.borrar_pantalla()
        print("Diamante agregado con exito.")
        sc.pausar_pantalla
