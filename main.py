from nivles import *

vidas = 3 
nivel = 1
puntos = 0
aciertos = 0
matriz_tablero = crear_matriz(None, 4, 4)
matriz_nivel_1 = cargar_diccionario_matriz(nivel_1)
while vidas != 0 and nivel < 6:
    # nivel = cargar_diccionario_matriz(nivel_1)
    # mostrar_matriz(nivel)
    print("---Bienvenidos a Agrupados ---")
    match nivel:
        case 1:
            
            mostrar_matriz(matriz_nivel_1)
            opciones_a_elegir = []
            
            while len(opciones_a_elegir) !=4 :
                fila = solicitar_entero("ingrese el numero de fila: ")
                columna = solicitar_entero("Ingrese el numero de columna: ")
                valor = mostrar_espesifica_matriz(matriz_nivel_1, fila -1, columna -1)
                cargar_vector(valor, opciones_a_elegir)
                
            if verificar_aciertos(opciones_a_elegir, nivel_1)!= True: #esta parte se puese hacer funsion, pasar tambien como parametros las vidas y los puntos 
                    vidas -= 1
                    print(f"Pierdes una vida")
            else:
                    puntos +=5
                    aciertos += 1
                    print("Sumas 5 puntos")
                    
            print(f"Tus puntos son: {puntos}")
            print(f"Tus vidas son: {vidas}")
            if aciertos == 4:
                nivel +=1        
        case 2:
            print("pasaste de nivel ")
        case 3:
            pass
        case 4:
            pass
        case 5:
            pass
        case _:
            pass 
print("Fin del juego..")