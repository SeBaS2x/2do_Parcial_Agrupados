import random
from archivos import *

def verificar_type(objeto, tipo)->bool:
    """Verificacion de type de un objeto

    Args:
        objeto (_type_): objeto a verificar
        tipo (_type_): type del objeto 

    Returns:
        bool: True o False
    """
    bandera= False
    if type(objeto) == tipo:
        bandera = True
    return bandera
def crear_matriz(valor,filas:int, columnas:int)->list:
    
    """Crea matriz con valores de inicializacion, filas y columnas.

    Args:
        valor (_type_): Valor de inicio de matriz
        filas (int):Cantidad de filas
        columnas (int): cantidad de columnas

    Returns:
        list: matriz 
    """
    matriz = [0] * filas
    for i in range(filas):
        matriz[i] = [0] * columnas
        for j in range(columnas):
            matriz[i][j] = valor
    return matriz

def cargar_diccionario_matriz(diccionario: dict):
    """Carga de manera aletoria las claves y valores de un diccionario en una matriz 

    Args:
        diccionario (dict): diccionario el cual cargar a la matriz

    Returns:
        _type_: matriz cargada
    """
    #categorías aleatorias sin repetir
    categorias = list(diccionario.keys())
    categorias_seleccionadas = random.sample(categorias, 4)

    # valores aleatorios de cada categoría 
    lista_total = []
    for categoria in categorias_seleccionadas:
        valores = diccionario[categoria]
        valores_elegidos = random.sample(valores, 4)   
        
        
        lista_total = lista_total + valores_elegidos

    
    random.shuffle(lista_total)

    
    matriz = []
    indice = 0
    for f in range(4):
        fila = lista_total[indice:indice+4]
        matriz += [fila]
        indice += 4

    return matriz

def mostrar_matriz(matriz:list):
    """Muestra una matriz, con la cantidad de filas y la cantidad de columnas como iundice 

    Args:
        matriz (list): matriz a mostrar
    """
    if verificar_type(matriz, list):
        filas = len(matriz)
        columnas = len(matriz[0])
        
        
        print("      ", end="")
        for j in range(columnas):
            print(f"Columna:{j+1:<10}", end=" ")
        print("")
        
        for i in range(len(matriz)):
            print(f"Fila: {i+1} ", end=" ")
            for j in range(len(matriz[i])):
                valor = matriz[i][j]
                if valor != None:
                    val = valor
                else:
                    val = " "
                print(f"{val:17}", end=" ")
            print("")
    else:
        print("Error al mostrar matriz")


def cargar_vector(valor:str, vector:list):
    """Carga valores dentro de un vector.

    Args:
        valor (str): valor a cargar
        vector (list): vector al cual se va cargar el valor

    Returns:
        _type_: _description_
    """
    if verificar_type(valor, str) and verificar_type(vector, list):
        vector += [valor]
        return vector
    else:
        print("Error de tipo de dato")
        
def cambiar_matriz_espacios_vacios(vector:list, matriz:list)->list:
    """actualiza matriz con espacios vacios que coinsidan con el vector
    Args:
        vector (list): vector de opciones a poner en blanco 
        matriz (list): matriz que se va a editar

    Returns matriz editada con espacios vacios
    """
    filas = len(matriz)
    columnas = len(matriz[0])
    matriz_vacia = crear_matriz(None, filas, columnas)
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            encontro = False
            for k in range(len(vector)):
                if matriz[i][j] == vector[k]:
                    encontro= True
                    break
            if encontro == False:
                    matriz_vacia[i][j] = matriz[i][j]
    return matriz_vacia


def solicitar_string(mensaje:str)->str:
    """Solicita un string con un input

    Args:
        mensaje (str): mensaje para solicitar 

    Returns:
        str: retorna la opcion ingresada
    """
    string = input(mensaje)
    return string

def parsear_a_minusculas(string: str)->str:
    """Parsear a minuscula todas las letras de un string

    Args:
        string (str): string a parsear

    Returns:
        str: _description_string parseado """
    if verificar_type(string, str):
        nuevo_string = ""
        for i in range(len(string)):
            id = ord(string[i])
            if id >= 65 and id <=90:
                nuevo_string += chr(id + 32)
            else:
                nuevo_string +=chr(id)
        return nuevo_string

def verificar_existencia_en_matriz(opcion:str, matriz:list)->bool:
    """verifica si una opcion esta dentro de la matriz y retorna un valor booleano

    Args:
        opcion (str): string a buscar en la matriz
        matriz (list): matitriz en cual buscar

    Returns:
        bool: True o False
    """
    if verificar_type(matriz, list) and verificar_type (opcion, str):
        encontro = False 
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                if matriz[i][j] == opcion:
                    encontro = True
                    break
        return encontro
def mostrar_vector(vector:list):
    """muestra vector, con valores que se van agregando 

    Args:
        vector (list): vector que mostrar
    """
    
    print(f"selecciono :{vector},\n")

def verificar_aciertos(opciones:list, diccionario:dict)->bool: 
    """verifica si una lista de opciones pertenece a los valores de un diccionario 

    Args:
        opciones (list): lista de opciones
        diccionario (dict): _deccionario en cual buscar

    Returns:
        bool: True o False
    """
    resultado = False
    if  verificar_type(opciones, list) and verificar_type(diccionario, dict) and len(opciones) == 4: 
    
        for clave in diccionario:
            lista_categoria = diccionario[clave]
            todos_en_categoria = True
            for opcion in opciones:
                encontrado = False
                for item in lista_categoria:
                    if opcion == item:
                        encontrado = True
                        break
                if not encontrado:
                    todos_en_categoria = False
                    break
            if todos_en_categoria:
                resultado = True
    else:
        print("Error..")
    return resultado

def mostrar_puntos_vidas( vidas:int, puntos:int):
    """muestra las vidas y puntos obtenidos

    Args:
        vidas (_type_): vidas que mostrar
        puntos (_type_): puntos que mostrar
    """
    print(f"Puntos obtenidos: {puntos}")
    print(f"Vidas: {vidas}")
    
def mostrar_categoria(matriz_tablero:list, diccionario:dict):
    """muestra un categoria y valor de un diccionario aleatoriamente

    Args:
        matriz_tablero (list):matriz en la cual buscar si conisiden los valores del diccionario
        diccionario (dict): diccionario en el cual comparar con la matriz

    Returns:
        _type_: retorna un string con la categoria y valor del diccionario 
    """
    for categoria in diccionario:
        valores = diccionario[categoria]
        
        indice = random.randint(0,len(valores)-1)
        valor_elegido = valores[indice]
        
        encontro = False
        for i in range(len(matriz_tablero)):
            for j in range(len(matriz_tablero[i])):
                if matriz_tablero[i][j] == valor_elegido:
                    encontro = True
                    break
            if encontro:
                break
        if encontro:
            mensaje = f"Categoria {categoria}, opcion: {valor_elegido}"
            return mensaje

