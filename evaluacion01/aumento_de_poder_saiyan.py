from personajes_por_raza import*
# Esta funcion lee e imprime los datos que tenga la lista parametrada en el primer parámetro.
# En el segundo parametro hacemos referencia a la caracteristica de los personajes que conformarn
# la lista.

def aumento_de_poder(lista_de_personajes):
    
    
    lista_de_saiyan = obtener_grupo_raza_personajes(lista_de_personajes,"raza")
 
    for raza,personaje in lista_de_saiyan.items():
        
        for personaje in personaje:
            if raza == "saiyan":
                nombre = personaje["nombre"]
                for personaje_saiyan in lista_de_personajes:
                    if personaje_saiyan["nombre"] == nombre:
                        
                        personaje_saiyan["poder_de_pelea"] = personaje_saiyan["poder_de_pelea"]*1.7
                        personaje_saiyan["poder_de_ataque"] = personaje_saiyan["poder_de_ataque"]*1.5
                        personaje_saiyan["habilidades"] += ' |transformación nivel dios'
     
                        with open("saiyan_cambiados.txt", "a") as archivo:
                                archivo.write(nombre + "\n")
                                
    print("Se agregaron los cambios a la raza saiyan.")
         
        