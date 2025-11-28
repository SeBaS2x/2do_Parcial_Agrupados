def cargar_dic_csv(ruta)->dict:
    diccionario = {}
    
    with open(ruta, "r", encoding= "utf-8") as archivo:
        archivo.readline()
        for linea in archivo:
            linea = linea.strip()
            
            categoria, valor = linea.split(",")
            
            if categoria not in diccionario:
                diccionario[categoria] = [valor]
            else:
                diccionario[categoria] = diccionario[categoria] + [valor]
    return diccionario

dic_juego_niveles= cargar_dic_csv("niveles.csv")

import json

def manejar_usuario(nombre, contraseña, puntos_obtenidos, archivo='usuarios.json', al_inicio=True):
    try:
        with open(archivo, 'r+') as file:
            data = json.load(file)
            
            if nombre in data:
                if al_inicio:
                    # Si es al inicio, no sumamos puntos
                    pass
                else:
                    # Si es al final, sumamos los puntos obtenidos
                    data[nombre]['puntos'] += puntos_obtenidos
            else:
                # Si el usuario no existe, lo creamos con la contraseña y los puntos (solo al final)
                data[nombre] = {'contraseña': contraseña, 'puntos': puntos_obtenidos if not al_inicio else 0}
            
            # Volver al principio y guardar los cambios
            file.seek(0)
            json.dump(data, file, indent=4)
            file.truncate()
    except FileNotFoundError:
        # Si el archivo no existe, lo creamos
        with open(archivo, 'w') as file:
            if al_inicio:
                data = {nombre: {'contraseña': contraseña, 'puntos': 0}}
            else:
                data = {nombre: {'contraseña': contraseña, 'puntos': puntos_obtenidos}}
            json.dump(data, file, indent=4)