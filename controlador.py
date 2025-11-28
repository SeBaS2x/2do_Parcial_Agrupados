from funciones import *

def ingreso_usuario(matriz_del_nivel,diccionario_juego):
    lista_vacia =[] 
    while len(lista_vacia) < 4:
        opcion = solicitar_string("Seleccione una Palabra o numero para elegir comodin: ")
        if len(opcion) == 1:
            ordenamiento = ord(opcion)
            if ordenamiento >= 48 and ordenamiento<= 57:
                opcion = int(opcion)
                match opcion:
                    case 1:
                        comodin_1 = mostrar_categoria(matriz_del_nivel, dic_juego_niveles)
                        print(comodin_1)
        opcion_parceada = parsear_a_minusculas(opcion)
        if verificar_existencia_en_matriz(opcion_parceada,matriz_del_nivel): 
            cargar_vector(opcion_parceada, lista_vacia)
            mostrar_vector(lista_vacia)
    return lista_vacia


def calcular_puntuacion(elecciones_del_usuario:list,matriz_nivel:list,diccionario_nivel:dict ,aciertos:int, puntaje:int, vida:int):
    if verificar_aciertos(elecciones_del_usuario ,diccionario_nivel): #verifica lista, suma punto, vidas y actualiza matriz
        matriz_nivel = cambiar_matriz_espacios_vacios(elecciones_del_usuario, matriz_nivel)
        aciertos += 1
        puntaje += 5
        mostrar_matriz(matriz_nivel)
        
    else:
        print("Opciones incorrectas. Se vuelve a intentar la ronda.")
        vida -=1
        elecciones_del_usuario = []
    return vida, puntaje, matriz_nivel, aciertos

def cargar_nivel(dic_juego_niveles:dict,puntos:int, vidas:int):
    aciertos = 0
    matriz_nivel_1 = cargar_diccionario_matriz(dic_juego_niveles)
    mostrar_matriz(matriz_nivel_1)
    while aciertos < 4 and vidas > 0:
        eleccion = ingreso_usuario(matriz_nivel_1,dic_juego_niveles)
        vidas, puntos, matriz_nivel_1, aciertos =calcular_puntuacion(eleccion,matriz_nivel_1,dic_juego_niveles,aciertos,puntos,vidas)  
    return vidas, puntos  