import json
import modules.utils.screenControlers as sc

def agregarZafiro():
    def id_existe(biblioteca, id_buscar):
        for zafiro in biblioteca["zafiro"]:
            if zafiro["id"] == id_buscar:
                return True
    with open ("./data/joyas.json","r",encoding="utf-8") as file:
            biblioteca=json.load(file)
    sc.borrar_pantalla()
    print("""
=========================================
        |Quilate del zafiro|
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
=========================================================
                |Factor de Tratamiento |   
=========================================================
Por favor ingrese el estado en que se encuentra el zafiro
1.Sin tratamiento (naturales y certificados)
2.Tratamiento térmico estándar
3.Tratamiento con relleno de vidrio                          
""")
    try:
        casoTR=int(input("->"))
        match casoTR:
            case 1:
                tratamiento=2.00
                trat="sin tratamiento"
            case 2:
                tratamiento=1.00
                trat="tratamiento termico estandar"
            case 3:
                tratamiento=0.50
                trat="Tratamiento con relleno de vidrio "
            case _:
                print("La eleccion ingresada no existe....")
    except ValueError:
        print("Por favor ingrese una eleccion valida...")
        sc.pausar_pantalla()
    sc.borrar_pantalla()
    print("""
==========================================
            |   Color|
==========================================
Por favor ingrese el color del zafiro.
1.Azul Royal
2.Azul vívido
3.Azul oscuro o claro
4.Zafiros de fantasía (rosa, amarillo, verde, etc.)
5.Padparadscha (rosa-naranja raro)                         
""")
    try:
        casoCL=int(input("->"))
        match casoCL:
            case 1:
                color=2.00
                coloor="Azul Royal"
            case 2:
                color=1.70
                coloor="Azul vívido"
            case 3:
                color=1.20
                coloor="Azul oscuro o claro"
            case 4:
                color=1.50
                coloor="Zafiros de fantasía"
            case 5:
                color=3.00
                coloor="adparadscha"
            case _:
                print("La eleccion ingresada no existe....")
    except ValueError:
        print("Por favor ingrese una eleccion valida...")
        sc.pausar_pantalla()
    sc.borrar_pantalla()
    print("""
========================================================
                     |Claridad|
========================================================
Por favor ingrese la claridad del zafiro.
1.Alta claridad (casi sin inclusiones visibles) 
2.Media claridad (inclusiones leves visibles con lupa)
3.Baja claridad (inclusiones visibles a simple vista)               
""")
    try:
            casoCLA=int(input("->"))
            match casoCLA:
                case 1:
                    claridad=1.50
                case 2:
                    claridad=1.20
                case 3:
                    claridad=0.80
                case _:
                    print("La eleccion ingresada no existe....")
                    sc.pausar_pantalla()
    except ValueError:
            print("Por favor ingrese una eleccion valida...")
            sc.pausar_pantalla()
    sc.borrar_pantalla()
    print("""
==========================================
            |Cantidad de zafiros|
==========================================
Ingrese la cantidad de zafiros.                 
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
    if quilate==0.50 and color==2.00:
        precioBQ1=2000
        precioBQ2=5000
    elif quilate==0.50 and color==1.70:
        precioBQ1=3000
        precioBQ2=7000
    elif quilate==0.50 and color==1.20:
        precioBQ1=500
        precioBQ2=1500
    elif quilate==0.50 and color==1.50:
        precioBQ1=800
        precioBQ2=3000
    elif quilate==0.50 and color==3.00:
        precioBQ1=5000
        precioBQ2=10000
    #1.00 quilates
    elif quilate==1.00 and color==2.00:
        precioBQ1=5000
        precioBQ2=8000
    elif quilate==1.00 and color==1.70:
        precioBQ1=7000
        precioBQ2=12000
    elif quilate==1.00 and color==1.20:
        precioBQ1=1500
        precioBQ2=3000
    elif quilate==1.00 and color==1.50:
        precioBQ1=1500
        precioBQ2=4000
    elif quilate==1.00 and color==3.00:
        precioBQ1=8000
        precioBQ2=15000
    #1.50 quilates
    elif quilate==1.50 and color==2.00:
        precioBQ1=6000
        precioBQ2=12000
    elif quilate==1.50 and color==1.70:
        precioBQ1=10000
        precioBQ2=18000
    elif quilate==1.50 and color==1.20:
        precioBQ1=2000
        precioBQ2=6000
    elif quilate==1.50 and color==1.50:
        precioBQ1=1800
        precioBQ2=5000
    elif quilate==1.50 and color==3.00:
        precioBQ1=9000
        precioBQ2=20000
    #2.00
    elif quilate==2.00 and color==2.00:
        precioBQ1=6500
        precioBQ2=15000
    elif quilate==2.00 and color==1.70:
        precioBQ1=12000
        precioBQ2=25000
    elif quilate==2.00 and color==1.20:
        precioBQ1=2500
        precioBQ2=7000
    elif quilate==2.00 and color==1.50:
        precioBQ1=2000
        precioBQ2=6000
    elif quilate==2.00 and color==3.00:
        precioBQ1=10000
        precioBQ2=25000
    if metal=="oro":
        valormetal=93.65*gramaje
    elif metal=="plata" :
        valormetal=1.05*gramaje
    elif metal=="no tiene":
        valormetal=0
    valorfinalmin=(((precioBQ1*(quilate**1.4)*tratamiento*claridad)*cantidadDiamantes)+valormetal)
    valorfinalmax=(((precioBQ2*(quilate**1.4)*tratamiento*claridad)*cantidadDiamantes)+valormetal)
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
    dicZafiro={"id":id,
                "quilate":quilate,
                "tratamiento":trat,
                "color":coloor,
                "cantidad":cantidadDiamantes,
                "metal":metal,
                "valorMin":int(valorfinalmin),
                "valorMax":int(valorfinalmax)}
    biblioteca["zafiro"].append(dicZafiro)
    with open ("./data/joyas.json","w") as k2:
        json.dump(biblioteca,k2,indent=4)
        sc.borrar_pantalla()
        print("zafiro agregado con exito.")
        sc.pausar_pantalla()
