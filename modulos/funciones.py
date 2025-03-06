import json

def agregarJoya(ruta,caso):
    try:
        with open (ruta,"r",encoding="utf-8") as file:
            biblioteca=json.load(file)
            match caso:
                case 1:
                    print("""
=========================================
      |Quilate de el diamante|
=========================================
Por favor ingrese quilate de el diamante.                         
""")
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
                        casoC=input(int(""))
                        match casoC:
                            case 1:
                                pass
                            case 2:
                                pass
                            case 3:
                                pass
                            case 4:
                                pass
                            case 5:
                                pass
                            case _:
                                print("La eleccion ingresada no existe....")
                                x=input("Presione enter para continuar.")
                    except ValueError:
                        print("Por favor ingrese una eleccion valida...")
                        x=input("Presione enter para continuar.")
                    print("""
==========================================
                |Color|
==========================================
Por favor ingrese el color del diamante.
1.Incoloro
2.Casi incoloro
3.Tono ligero
4.Marron/Amarillo
5.Fantasia(Azul, Rosa, Verde, Amarillo intenso, Rojo.)                         
""")
                    try:
                        casoCL=input(int(""))
                        match casoCL:
                            case 1:
                                pass
                            case 2:
                                pass
                            case 3:
                                pass
                            case 4:
                                pass
                            case 5:
                                pass
                            case _:
                                print("La eleccion ingresada no existe....")
                                x=input("Presione enter para continuar.")
                    except ValueError:
                        print("Por favor ingrese una eleccion valida...")
                        x=input("Presione enter para continuar.")
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
                            casoCla=input(int(""))
                            match casoCla:
                                case 1:
                                    pass
                                case 2:
                                    pass
                                case 3:
                                    pass
                                case 4:
                                    pass
                                case 5:
                                    pass
                                case _:
                                    print("La eleccion ingresada no existe....")
                                    x=input("Presione enter para continuar.")
                        except ValueError:
                            print("Por favor ingrese una eleccion valida...")
                            x=input("Presione enter para continuar.")
    except Exception as e :
        print("error al agregar informacion de joya...")
        x=input ("presione en ter para continuar")
        return agregarJoya()