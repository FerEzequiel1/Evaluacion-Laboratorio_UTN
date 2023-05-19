import random
from datetime import datetime

# Jugar batalla: El usuario seleccionará un personaje,el cual se enviara a la funcion como segundo parametro.
# Dentro de la funcion seleccionamos otro al azar. Gana la batalla el personaje que más poder de ataque tenga. 
# El personaje que gana la batalla se guardarda en un archivo de texto, con fecha de la batalla, 
# el nombre del personaje que ganó y el nombre del perdedor. Este archivo anexará cada vez que se use.

def batalla_entre_personajes(lista_de_personajes,retador):
    retador = retador.lower()
    for personaje in lista_de_personajes:
        if personaje["nombre"] == retador:
            confirmar_existencia = True
            break
        else:
            confirmar_existencia = False
            
    if confirmar_existencia:
        
        personaje_random = random.randint(1,len(lista_de_personajes))
        revelacion_contricante = lista_de_personajes[personaje_random]
        peleador_local = revelacion_contricante["nombre"]
        
        
        
        while peleador_local == retador:
            
            personaje_random = random.randint(1,len(lista_de_personajes))
            revelacion_contricante = lista_de_personajes[personaje_random]
            peleador_local = revelacion_contricante["nombre"]
            
        for personaje in lista_de_personajes:
            if retador == personaje["nombre"]:
                retador = personaje["nombre"]
                poder_de_ataque = personaje["poder_de_ataque"]
            if peleador_local == personaje["nombre"]:
                peleador_local = personaje["nombre"]
                poder_de_ataque_local = personaje["poder_de_ataque"] 
        
        if poder_de_ataque > poder_de_ataque_local:
            print(f"{retador} gana ante {peleador_local}.")  
            ganador = retador
            perdedor = peleador_local
        else:
            print(f"{retador} pierde ante {peleador_local}.")
            ganador = peleador_local
            perdedor = retador
            
        guardar_resultado_batalla(ganador,perdedor)  #Se guarda al ganador
        
    else:
        print("Ese peleador no existe")
        
        
# Se llama dandole como primer parametro la lista de los personajes y como segundo
# el personaje que queremos que pelee por el usuario

# pelador_elegido = input("Ingrese el peleador que quiere que combata")
# batalla_entre_personajes(datos,"Gotenks"
        
        
# Esta funcion guarda  el resultado de la batalla del punto 5,recibe como primer parametro
# al ganador,y como segundo parametro al perdedor.
        
def guardar_resultado_batalla(ganador, perdedor):
    
    fecha_actual = datetime.now().strftime("%d-%m-%Y")
    resultado = f"{fecha_actual} - Ganador: {ganador}  Perdedor: {perdedor}"
    
    with open("resultados_batallas.txt", "a") as archivo:
        archivo.write(resultado + "\n")   
        
        
