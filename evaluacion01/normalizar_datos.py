import re

# Con esta funcion se normaliza los datos con los que vamos a trabajar para poder manipularlos.
# recibe como parametros los datos que queremos normalizar y devuelve una lista de diccionarios 
# de los elementos que tengamos


def obtener_datos(datos:str)->list:
    lista = []
    
    archivo = open(datos,"r",encoding="utf-8")
    
    for linea in archivo:
        ordenamiento = re.split(",|\n",linea)
        diccionario ={}
        diccionario["id"] = int(ordenamiento[0])
        diccionario["nombre"] = ordenamiento[1].lower()
        diccionario["raza"] = ordenamiento[2].lower()
        diccionario["poder_de_pelea"] = int(ordenamiento[3])
        diccionario["poder_de_ataque"] = int(ordenamiento[4])
        habilidades= re.sub(r'\|\$%', '|', ordenamiento[5])
        diccionario["habilidades"] = habilidades.lower()
        lista.append(diccionario)
        
    archivo.close()
    
    print("Archivos normalizados para su uso. ")
    return lista

# Se usa de esta forma dandole como parámetro la lista que queremos normalizar
# datos = obtener_datos("DBZ.csv")
