# Esta funcion muestra todas las razas indicando la cantidad de personajes que
# corresponden a esa raza. 

def obtener_cantidad_por_raza(datos):
    lista_raza_por_personaje = {}
    
    for personaje in datos:
        raza = personaje["raza"]
        if raza not in lista_raza_por_personaje:
            lista_raza_por_personaje[raza] = 1
        else:
            lista_raza_por_personaje[raza] += 1
    

    for raza, cantidad in lista_raza_por_personaje.items():
        print(f"{raza}: {cantidad}")
        
# Se usa dandole como parámetro la lista en donde 
# querramos sacar los datos
#obtener_cantidad_por_raza(datos)