from lista_cantidad_por_raza import*
from personajes_por_raza import*
from batallas import*
from guardar_personaje import*
from nombre_por_habilidad import*
from normalizar_datos import*
from aumento_de_poder_saiyan import*

seguir = True

menu = ["1-Traer datos del archivo. ",
        "2-Mostrar todas las razas indicando la cantidad de personajes que corresponden a esa raza. ",
        "3-Mostrar cada raza indicando el nombre y poder de ataque de cada personaje. ",
        "4-Ingresa la descripción de una habilidad y mostrar nombre, raza y promedio de poder entre ataque y defensa de personajes con esa habilidad: ",
        "5-Pelea entre personajes. ",
        "6-Guardar personajes por raza y habiliad ingresada. ",
        "7-Mostrar personajes guardados de la opcion 6: ",
        "8-Aumentar el poder de ataque y pelea a la raza saiyan y agregar la habilidad 'transformación nivel dios'.",
        "9-Salir."
        ]

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
                    pelador_elegido = input("Ingrese el peleador que quiere que combata : ")
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
                if normalizar_dato:
                    aumento_de_poder(datos)  
                else:
                    print("Debes normalizar los datos en el punto 1 antes de realizar esta accion")
            case 9:
                break
            
mostrar_menu("DBZ.csv")
