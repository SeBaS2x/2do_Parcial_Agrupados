import random
nivel_1 = {
    "deportes": ["fútbol", "tenis", "basket", "natacion"],
    "peliculas": ["accion", "rpg", "estrategia", "aventura"],
    "paises": ["argentina", "brasil", "paraguay", "uruguay"],
    "intrumentos": ["guitarra", "piano", "violin", "trompeta"]
}
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
    matriz = [[valor]* columnas for _ in range(filas)]
    return matriz
def mostrar_matriz(matriz:list):
    """Valida y muestra la Matriz que se le pase a la funcion. Print() a la salida
    Args:
        matriz (list): Matriz a mostrar.
    """
    if verificar_type(matriz, list):
        for i in range(len(matriz)):
            for j in range(len(matriz[0])):
                print(f"{matriz[i][j]:17}", end=" ")
            print("")
    else:
        print("Error al mostrar Matriz")
def cargar_diccionario_matriz(diccionario: dict)->list:
    lista_total = []
    for categoria in diccionario:
        lista = diccionario[categoria]
        for valor in lista:
            lista_total += [valor]
    random.shuffle(lista_total)
    matriz = crear_matriz(None, len(diccionario[categoria]),len(lista))
    idx = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = lista_total[idx]
            idx += 1
    return matriz
# lista = cargar_diccionario_matriz(nivel_1)
# mostrar_matriz(lista)

def verificar_aciertos(opciones:list, diccionario:dict)->bool:
    for clave in diccionario:
        verificador = diccionario[clave]
        bandera = True
        for elemento in opciones:
            if elemento not in verificador:
                bandera= False
                break
        if bandera:
            break
    return bandera
        

def solicitar_string(mensaje:str)->str:
    """Solicita un string con un input

    Args:
        mensaje (str): mensaje para solicitar 

    Returns:
        str: retorna la opcion ingresada
    """
    string = input(mensaje)
    return string
def solicitar_entero(mensaje:str):
    """solicita el ingreso de un numero entero.

    Args:
        mensaje (str): _mensaje para pedir el numero

    Returns:
        int: Numero ingresado
    """
    numero = input(mensaje)
    return int(numero)

def cargar_vector(valor:int, vector:list):
    
        vector += [valor]
        return vector

# lista = []
# while len(lista)!=3:
#     numero = solicitar_entero("entero:")
#     cargar_vector(numero,lista)
# print(lista)

def mostrar_espesifica_matriz(matriz:list, fila:int, columna:int)->int:
    """Muestra un valor especifico de una matriz

    Args:
        matriz (list): matriz con valores cargados  
        fila (int): Fila en que buscar
        columna (int): columna en que buscar

    Returns:
        int: Valor encontrado
    """

    valor = matriz[fila][columna]
    return valor