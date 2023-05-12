import re
import random
import json
from datetime import datetime



seguir = True

# 1
# Con esta funcion se normaliza los datos con los que vamos a trabajar para poder manipularlos.
# recibe como parametros los datos que queremos normalizar y devuelve una lista de diccionarios 
# de los elementos que tengamos
def cofirmar_inicializacion():
    return True

def obtener_datos(datos:str)->list:
    lista = []
    
    archivo = open(datos,"r",encoding="utf-8")
    
    for linea in archivo:
        ordenamiento = re.split(",|\n",linea)
        diccionario ={}
        diccionario["id"] = int(ordenamiento[0])
        diccionario["nombre"] = ordenamiento[1]
        diccionario["raza"] = ordenamiento[2]
        diccionario["poder_de_pelea"] = int(ordenamiento[3])
        diccionario["poder_de_ataque"] = int(ordenamiento[4])
        habilidades= re.sub(r'\|\$%', '|', ordenamiento[5])
        diccionario["habilidades"] = habilidades
        lista.append(diccionario)
        
    archivo.close()
    return lista

# Se usa de esta forma dandole como parámetro la lista que queremos normalizar
# datos = obtener_datos("./integrador00/DBZ.csv")


# 2
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

# Se usa de esta manera,dandole como parámetro la lista en donde 
# querramos sacar los datos
#obtener_cantidad_por_raza(datos)


# 3
# Esta funcion retornara en una lista cada raza indicando el nombre y poder de ataque de cada
# personaje que la corresponda.

def obtener_grupo_raza_personajes(lista_personajes,caracteristica):

    lista_de_caracteristicas = {}

    for personaje in lista_personajes:
        caracteristica_lista = re.split('-',personaje[caracteristica])  
        nombre = personaje['nombre']
        poder_ataque = personaje['poder_de_ataque']
        
        if caracteristica_lista == ['Three', 'Eyed People']:
            caracteristica_lista= ['Three-Eyed People']
        elif caracteristica_lista == ['Shin','jin']:
            caracteristica_lista = ['Shin-jin']
        
        for raza in caracteristica_lista:
            if raza not in lista_de_caracteristicas:
                lista_de_caracteristicas[raza] = [{'nombre':nombre, 'poder_de_ataque': poder_ataque}]
            else:
                lista_de_caracteristicas[raza].append({'nombre': nombre, 'poder_de_ataque': poder_ataque})


    return lista_de_caracteristicas
       
    
# grupo_raza = obtener_grupo_raza_personajes(datos,"raza")


# Esta funcion lee e imprime los datos que tenga la lista parametrada en el primer parámetro.
# En el segundo parametro hacemos referencia a la caracteristica de los personajes que conformarn
# la lista.

def leer_personajes_por_raza(lista,caracteristica):
    for raza, personajes in lista.items():
        print(caracteristica.capitalize()+":"+raza)
        for personaje in personajes:
            print(f"Nombre: {personaje['nombre']}, Poder de Ataque: {personaje['poder_de_ataque']}")
        print()
    
# leer_personajes_por_raza(grupo_raza,"raza")    

#  4
# En esta funcion el usuario ingresa la descripción de una habilidad y se muestra
# el nombre, raza y promedio de poder entre ataque y pelea de todos los personajes
# que tengamos en nuestra lista que usen esa habilidad .

def obtener_personajes_de_habilidad(lista_de_personajes,habilidad):
    
    lista_de_personajes_con_habilidad =[]
    habilidad = habilidad.capitalize()
   
    
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


# 5
# Jugar batalla: El usuario seleccionará un personaje,el cual se enviara a la funcion como segundo parametro.
# Dentro de la funcion seleccionamos otro al azar. Gana la batalla el personaje que más poder de ataque tenga. 
# El personaje que gana la batalla se guardarda en un archivo de texto, con fecha de la batalla, 
# el nombre del personaje que ganó y el nombre del perdedor. Este archivo anexará cada vez que se use.

def batalla_entre_personajes(lista_de_personajes,retador):
    
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
            
        guardar_resultado_batalla(ganador,perdedor) 
        
    else:
        print("Ese peleador no existe")

# Se llama dandole como primer parametro la lista de los personajes y como segundo
# el personaje que queremos que pelee por el usuario

# pelador_elegido = input("Ingrese el peleador que quiere que combata")
# batalla_entre_personajes(datos,"Gotenks")
 
  
# Esta funcion guarda  el resultado de la batalla del punto 5,recibe como primer parametro
# al ganador,y como segundo parametro al perdedor.
      
def guardar_resultado_batalla(ganador, perdedor):
    
    fecha_actual = datetime.now().strftime("%d-%m-%Y")
    resultado = f"{fecha_actual} - Ganador: {ganador}  Perdedor: {perdedor}"
    
    with open("resultados_batallas.txt", "a") as archivo:
        archivo.write(resultado + "\n")   
    

# 6

# El usuario ingresa una raza y una habilidad.Esta funcion genera un listado de los personajes que
# cumplan con los dos criterios ingresados, los mismos se guardarán en un archivo Json. 
# Se guarda el nombre del personaje, el poder de ataque, y las habilidades que no fueron parte de la
# búsqueda. El nombre del archivo estará nomenclado con la descripción de la habilidad y de la raza y sera
# devuelto en el retorno da la funcion para usarlo si el usario lo requiere

def obtener_personaje_ingresado(raza_ingresada,habilidad,lista):
    
    
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

#  7. 
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


# Esta funcion recibe como parametro la respuesta del usario cuando ingresa una opcion
# se verifica que sea de tipo numerico y que el valor sea dentro del rango para elegir

def menu_principal(menu):
    
    for opcion in menu:
        print(opcion)
    
    opcion = input("Ingrese una opcion: ")
   
    if opcion.isnumeric():
        valor_opcion = int(opcion)
        if valor_opcion >9:
            return False
        else:
            return valor_opcion
    else:
        return False


menu = ["1-Traer datos del archivo. ",
        "2-Mostrar todas las razas indicando la cantidad de personajes que corresponden a esa raza. ",
        "3-Mostrar cada raza indicando el nombre y poder de ataque de cada personaje. ",
        "4-Ingresa la descripción de una habilidad y mostrar nombre, raza y promedio de poder entre ataque y defensa de personajes con esa habilidad: ",
        "5-Pelea entre personajes. ",
        "6-Guardar personajes por raza y habiliad ingresada. ",
        "7-Mostrar personajes guardados de la opcion 6: ",
        "8-Salir."]


def mostrar_menu(dato_fuente):
    normalizar_dato = False
    datos_guardados = False
    
    while seguir == True:
        print("")
        opciones=menu_principal(menu)
        print("")

        while opciones == False:
            print("")
            print("Valor incorrecto.Ingrese un número de las opciones mostradas.")
            opciones=menu_principal(menu)
            print("")
        match opciones:
            case 1:
                datos = obtener_datos(dato_fuente)
                normalizar_dato = True
            case 2:
                
                if normalizar_dato:
                    obtener_cantidad_por_raza(datos) 
                else:
                    print("Debes normalizar los datos en el punto 1 antes de realizar esta accion")
                    
            case 3:
                if normalizar_dato:
                    grupo_raza = obtener_grupo_raza_personajes(datos,"raza")
                    leer_personajes_por_raza(grupo_raza,"raza")    
                else:
                    print("Debes normalizar los datos en el punto 1 antes de realizar esta accion")
                
            case 4:
                if normalizar_dato:
                    habilidad_ingresada =input("Ingrese una habilidad: ")
                    obtener_personajes_de_habilidad(datos,habilidad_ingresada)    
                else:
                    print("Debes normalizar los datos en el punto 1 antes de realizar esta accion")
                
            case 5:
                if normalizar_dato:
                    pelador_elegido = input("Ingrese el peleador que quiere que combata con sus iniciales en MAYUSCULA: ")
                    batalla_entre_personajes(datos,pelador_elegido)    
                else:
                    print("Debes normalizar los datos en el punto 1 antes de realizar esta accion")
                
            case 6:
                if normalizar_dato:
                    raza = input("Ingrese la raza que quiere buscar: ")
                    habilidad = input("Ingrese la habilidad que quiere buscar dentro de esa raza: ")
                    busqueda_raza_con_habilidad = obtener_personaje_ingresado(raza,habilidad,datos)
                    datos_guardados = True   
                else:
                    print("Debes normalizar los datos en el punto 1 antes de realizar esta accion")
                
            case 7:
                if normalizar_dato :
                    if datos_guardados:
                        obtener_ultimo_json(busqueda_raza_con_habilidad) 
                    else:
                        print("Debes utilizar la opción 6 antes de utilizar esta. ")
                else:
                    print("Debes normalizar los datos en el punto 1 antes de realizar esta accion")
            case 8:
                break
            
mostrar_menu("./evaluacion01/DBZ.csv")
