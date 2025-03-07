import json
import utils.screenControlers as sc

def agregarJoya(ruta,caso):
        with open (ruta,"r",encoding="utf-8") as file:
            biblioteca=json.load(file)
            match caso:
                case 1:
                    
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
                        casoC=input(int("->"))
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
                                sc.pausar_pantalla()
                    except ValueError:
                        print("Por favor ingrese una eleccion valida...")
                        sc.pausar_pantalla()
                    quilate=input(float(""))
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
                        casoC=input(int("->"))
                        match casoC:
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
                                sc.pausar_pantalla()
                    except ValueError:
                        print("Por favor ingrese una eleccion valida...")
                        sc.pausar_pantalla()
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
                        casoCL=input(int("->"))
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
                                sc.pausar_pantalla()
                    except ValueError:
                        print("Por favor ingrese una eleccion valida...")
                        sc.pausar_pantalla()
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
                            casoCla=input(int("->"))
                            match casoCla:
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
                                    x=input("Presione enter para continuar.")
                        except ValueError:
                            print("Por favor ingrese una eleccion valida...")
                            sc.pausar_pantalla()
                        precioBQ=0
                        if quilate==0.20 and color=="d-f":
                            pass
        print("error al agregar informacion de joya...")
        sc.pausar_pantalla()
        return agregarJoya()