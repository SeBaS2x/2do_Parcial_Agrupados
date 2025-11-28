from funciones import *
from controlador import *
from archivos import *
import sys
def main() -> None:
    vidas = 3 
    nivel = 1
    puntos = 0
    nombre =input("Ingrese nombre de Ususario:")
    contraseña = input("Ingrese contraseña: ")
    manejar_usuario(nombre, contraseña , 0, al_inicio= True)
    print("---Bienvenidos a Agrupados ---")
    while vidas != 0 and nivel < 6:
        match nivel:
            case 1:
                print("Nivel 1")
                print("Comodines:\n 1.Revelar categoría")
                vidas, puntos = cargar_nivel(dic_juego_niveles,puntos, vidas)
                mostrar_puntos_vidas(vidas,puntos)
                nivel +=1        
            case 2:
                print("NIVEL 2 ")
                print("Comodines:\n 1.Revelar categoría")
                vidas, puntos = cargar_nivel(dic_juego_niveles,puntos, vidas)
                mostrar_puntos_vidas(vidas,puntos)
                nivel +=1  
            case 3:
                print("NIVEL 3 ")
                print("Comodines:\n 1.Revelar categoría")
                vidas, puntos = cargar_nivel(dic_juego_niveles,puntos, vidas)
                mostrar_puntos_vidas(vidas,puntos)
                nivel +=1  
            case 4:
                print("NIVEL 4 ")
                print("Comodines:\n 1.Revelar categoría")
                vidas, puntos = cargar_nivel(dic_juego_niveles,puntos, vidas)
                mostrar_puntos_vidas(vidas,puntos)
                nivel +=1  
            case 5:
                print("NIVEL 5 ")
                print("Comodines:\n 1.Revelar categoría")
                vidas, puntos = cargar_nivel(dic_juego_niveles,puntos, vidas)
                mostrar_puntos_vidas(vidas,puntos)
                nivel +=1  
            case _:
                pass 
    manejar_usuario(nombre, contraseña, puntos, al_inicio=False)

    print("Fin del juego..")

if __name__ == "__main__":
    sys.exit(main())