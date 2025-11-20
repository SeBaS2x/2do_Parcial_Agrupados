import random
nivel_1 = {
    "deportes": ["futbol", "tenis", "basket", "natacion"],
    "videojuegos": ["accion", "rpg", "estrategia", "aventura"],
    "paises": ["argentina", "brasil", "paraguay", "uruguay" ],
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
    matriz = [0] * filas
    for i in range(filas):
        matriz[i] = [0] * columnas
        for j in range(columnas):
            matriz[i][j] = valor
    return matriz
    
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

def mostrar_matriz(matriz:list):
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
    if verificar_type(valor, str) and verificar_type(vector, list):
        vector += [valor]
        return vector
    else:
        print("Error de tipo de dato")
        
def cambiar_matriz_espacios_vacios(vector:list, matriz:list)->list:
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
    if verificar_type(string, str):
        nuevo_string = ""
        for i in range(len(string)):
            id = ord(string[i])
            if id >= 65 and id <=90:
                nuevo_string += chr(id + 32)
            else:
                nuevo_string +=chr(id)
        return nuevo_string
    else:
        print("Error de tipo de dato")
        
def verificar_existencia_en_matriz(opcion:str, matriz:list)->bool:
    
    if verificar_type(matriz, list) and verificar_type (opcion, str):
        encontro = False 
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                if matriz[i][j] == opcion:
                    encontro = True
                    break
        return encontro
def mostrar_vector(vector:list):
    
    
        print(f"selecciono :{vector},\n")

def verificar_aciertos(opciones:list, diccionario:dict)->bool: 
    """_summary_

    Args:
        opciones (list): _description_
        diccionario (dict): _description_

    Returns:
        bool: _description_
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

def mostrar_puntos_vidas( vidas, puntos):
    print(f"Puntos obtenidos: {puntos}")
    print(f"Vidas: {vidas}")