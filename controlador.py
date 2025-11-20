from funciones import *

def ingreso_usuario(matriz_del_nivel):
    lista_vacia =[] ###pide dato y carga en lista    ## lista vacia, 
    while len(lista_vacia) < 4:
        opcion = solicitar_string("Seleccione una Palabra: ") #Guardar en variable y pasar parametro
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