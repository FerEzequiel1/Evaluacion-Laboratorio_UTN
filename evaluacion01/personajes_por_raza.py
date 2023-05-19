import re

# Esta funcion retornara en una lista cada raza indicando el nombre y poder de ataque de cada
# personaje que la corresponda.

def obtener_grupo_raza_personajes(lista_personajes,caracteristica):

    lista_de_caracteristicas = {}

    for personaje in lista_personajes:
        caracteristica_lista = re.split('-',personaje[caracteristica])  
        nombre = personaje['nombre']
        
        poder_ataque = personaje['poder_de_ataque']
        
        if caracteristica_lista == ['three', 'eyed People']:
            caracteristica_lista= ['three-Eyed people']
        elif caracteristica_lista == ['shin','jin']:
            caracteristica_lista = ['shin-jin']
        
        for raza in caracteristica_lista:
            if raza not in lista_de_caracteristicas:
                lista_de_caracteristicas[raza] = [{'nombre':nombre, 'poder_de_ataque': poder_ataque}]
            else:
                lista_de_caracteristicas[raza].append({'nombre': nombre, 'poder_de_ataque': poder_ataque})


    return lista_de_caracteristicas


def leer_personajes_por_raza(lista,caracteristica):
    for raza, personajes in lista.items():
        print(caracteristica.capitalize()+":"+raza)
        for personaje in personajes:
            print(f"Nombre: {personaje['nombre']}, Poder de Ataque: {personaje['poder_de_ataque']}")
        print()