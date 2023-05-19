import json
import re
from personajes_por_raza import*

# El usuario ingresa una raza y una habilidad.Esta funcion genera un listado de los personajes que
# cumplan con los dos criterios ingresados, los mismos se guardarán en un archivo Json. 
# Se guarda el nombre del personaje, el poder de ataque, y las habilidades que no fueron parte de la
# búsqueda. El nombre del archivo estará nomenclado con la descripción de la habilidad y de la raza y sera
# devuelto en el retorno da la funcion para usarlo si el usario lo requiere


def obtener_personaje_ingresado(raza_ingresada,habilidad,lista):
    
    raza_ingresada = raza_ingresada.lower()
    habilidad = habilidad.lower()
    
    lista_de_personajes = obtener_grupo_raza_personajes(lista,"raza")    
    lista_personajes_con_habilidades = []
    personajes_formateados = []
    
    for raza,personajes in lista_de_personajes.items():
        if raza == raza_ingresada:
            for personaje in personajes:
                for personaje_lista in lista:
                    if (personaje['nombre'] == personaje_lista["nombre"]) and re.search(habilidad,personaje_lista["habilidades"]):
                        habilidades = personaje_lista["habilidades"]
                        perro ={}
                        perro["nombre"]=personaje['nombre']
                        perro["poder_de_ataque"] = personaje['poder_de_ataque']
                        perro['habilidades'] = habilidades.replace("|","+")
                        lista_personajes_con_habilidades.append(perro)
                       
    if len(lista_personajes_con_habilidades)>0:
           
        for personaje in lista_personajes_con_habilidades:
            formateo_personaje = {}
            formateo_personaje["nombre"] = personaje['nombre']
            formateo_personaje["poder_de_ataque"] = personaje['poder_de_ataque']
            formateo_personaje['habilidades'] = personaje['habilidades']
            personajes_formateados.append(formateo_personaje)
        print("Datos guardados correctamente. ") 
    else:
        print("No se encontro una raza con esa habiidad") 
    

# Guardar en archivo JSON
    
    formato_nombre_de_habilidad = habilidad
    formato_nombre_de_habilidad = formato_nombre_de_habilidad.replace(" ","_")
    
    formato_nombre_de_raza = raza_ingresada
    formato_nombre_de_raza = formato_nombre_de_raza.replace(" ","_")
    formato_nombre_de_raza = formato_nombre_de_raza.replace("-","_")
    
    
    
    nombre_archivo_json = '_'.join([formato_nombre_de_raza, formato_nombre_de_habilidad])
    if len(personajes_formateados)>0:
        with open(f"{nombre_archivo_json}.json", "w",encoding="utf-8") as archivo:
            json.dump(personajes_formateados, archivo, indent=4) 
    
    return nombre_archivo_json

# Se utiliza dandole como parámetro la raza que quiere buscar,la habilidad,y la lista de nuestros personajes
# la raza y habilidad se piden pediante un input

# busqueda_raza_con_habilidad = obtener_personaje_ingresado("Saiyan","Kamehameha",datos)




# Esta funcion permitirá mostrar el listado de los personajes guardados en el archivo Json de la opción
# 6.

def obtener_ultimo_json(jsons):
    
    with open(f'{jsons}.json') as file:
         data = json.load(file)
    
    for personaje in data:
        
        nombre = personaje['nombre']
        poder_de_ataque = personaje['poder_de_ataque']
        habilidades = personaje['habilidades']
        print(f"{nombre} - {poder_de_ataque} - {habilidades}")
        
        
# Se usa con esta funcion donde se recibe como parametro el valor de retorno de la funcion
# del punto 6      
# obtener_ultimo_json(busqueda_raza_con_habilidad) 
        
        
        
