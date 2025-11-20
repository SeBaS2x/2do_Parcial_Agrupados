
from funciones import *
from controlador import *
vidas = 3 
nivel = 1
puntos = 0
aciertos = 0



print("---Bienvenidos a Agrupados ---")
while vidas != 0 and nivel < 6:
    
    match nivel:
        case 1:
            print("Nivel 1")
            matriz_nivel_1 = cargar_diccionario_matriz(nivel_1)
            mostrar_matriz(matriz_nivel_1)
            while aciertos < 4:
                eleccion = ingreso_usuario(matriz_nivel_1)
                vidas, puntos, matriz_nivel_1, aciertos =calcular_puntuacion(eleccion,matriz_nivel_1,nivel_1,aciertos,puntos,vidas)  
                mostrar_puntos_vidas(vidas,puntos)
            nivel +=1
            
        case 2:
            print("NIVEL 2 ")
            matriz_nivel_2 = cargar_diccionario_matriz(nivel_1)
            mostrar_matriz(matriz_nivel_2)
            while aciertos < 4:
                eleccion = ingreso_usuario(matriz_nivel_2)
                vidas, puntos, matriz_nivel_2, aciertos =calcular_puntuacion(eleccion,matriz_nivel_2,nivel_1,aciertos,puntos,vidas)  
                mostrar_puntos_vidas(vidas,puntos)
            nivel +=1
        case 3:
            print("NIVEL 3 ")
            matriz_nivel_3 = cargar_diccionario_matriz(nivel_1)
            mostrar_matriz(matriz_nivel_3)
            while aciertos < 4:
                eleccion = ingreso_usuario(matriz_nivel_3)
                vidas, puntos, matriz_nivel_3, aciertos =calcular_puntuacion(eleccion,matriz_nivel_3,nivel_1,aciertos,puntos,vidas)  
                mostrar_puntos_vidas(vidas,puntos)
            nivel +=1
        case 4:
            print("NIVEL 4 ")
            matriz_nivel_4 = cargar_diccionario_matriz(nivel_1)
            mostrar_matriz(matriz_nivel_4)
            while aciertos < 4:
                eleccion = ingreso_usuario(matriz_nivel_4)
                vidas, puntos, matriz_nivel_4, aciertos =calcular_puntuacion(eleccion,matriz_nivel_4,nivel_1,aciertos,puntos,vidas)  
                mostrar_puntos_vidas(vidas,puntos)
            nivel +=1
        case 5:
            print("NIVEL 5 ")
            matriz_nivel_5 = cargar_diccionario_matriz(nivel_1)
            mostrar_matriz(matriz_nivel_5)
            while aciertos < 4:
                eleccion = ingreso_usuario(matriz_nivel_5)
                vidas, puntos, matriz_nivel_5, aciertos =calcular_puntuacion(eleccion,matriz_nivel_5,nivel_1,aciertos,puntos,vidas)  
                mostrar_puntos_vidas(vidas,puntos)
            nivel +=1
        case _:
            pass 
print("Fin del juego..")