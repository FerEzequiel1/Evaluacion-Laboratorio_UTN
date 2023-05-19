import re
# En esta funcion el usuario ingresa la descripción de una habilidad y se muestra
# el nombre, raza y promedio de poder entre ataque y pelea de todos los personajes
# que tengamos en nuestra lista que usen esa habilidad .

def obtener_personajes_de_habilidad(lista_de_personajes,habilidad):
    
    lista_de_personajes_con_habilidad =[]
    habilidad = habilidad.lower()
    
   
    
    for personaje in lista_de_personajes:
        
        habilidad_de_personaje = personaje['habilidades']
        if re.search(habilidad, habilidad_de_personaje):
            personajes = {}
            personajes["nombre"] = personaje["nombre"]
            personajes["raza"] = personaje["raza"]
            poder_ataque = personaje["poder_de_ataque"]
            poder_pelea = personaje["poder_de_pelea"]
            promedio = round((poder_ataque+poder_pelea)/2,2)
            personajes["promedio"] = promedio
            lista_de_personajes_con_habilidad.append(personajes)
        
            
    if len(lista_de_personajes_con_habilidad)>0:      
        print(f"Personajes que usan {habilidad.capitalize()}:")   
        for personaje in lista_de_personajes_con_habilidad:
            print(f"Nombre:{personaje['nombre']}  Raza:{personaje['raza']}  Promedio de ataque y pelea:{personaje['promedio']}")
    else:
        print(f"No se encontro algun personaje con la habilidad {habilidad.capitalize()}")
                   
                   
# Se usa iniciando con la la variable 'habilidad_ingresada' que pregunta al usuario,la habilidad 
# que quiere buscar. Luego,se introduce esta variable como segundo parametro de la funcion.El primer
# parametro es nuestra lista de personajes.

# habilidad_ingresada =input("Ingrese una habilidad: ")
# obtener_personajes_de_habilidad(datos,habilidad_ingresada)
