
#importacionq eu nos permite abrir archivos 
import codecs
#IMportacion qeu permite convertir los arhivos en archivos.json
import json
#Almacenacion en una variable luego de abrir un archivo
archivo = codecs.open("datos.txt", "r")
#leE CADA UNA DE LAS LINEAS 
lineas = archivo.readlines()
#Imprime el numero de lineas
print(len(lineas))
#Transforma cada una de las lineas en diccionarios 
lin_diccionario = [json.loads(l) for l in lineas]
#Funcion anonima que permite comparar el pais es igual Nigeria, (Pertenece a Nigeria)
funcion1 = lambda x: list(x.items())[0][1] == "Nigeria"
#Impresion 	que filtra la funcion 1 y la imprime a los que pertenecen a Nigeria 
print("Lista de Jugadores que pertenecen a Nigeria")
print(list(filter(funcion1, lin_diccionario)))
#Funcion anonima que me co9mpara los que tienen goles mayor a 3
funcion2 =  lambda x: x["Goals"] > 3
print("Lista de Jugadores que han hecho mas de 3 Goles")
#Impresion de la funcion2 filtrando los qeu tienen mayor a 3 goles
print(list(filter(funcion2, lin_diccionario)))

#Accede directamente a los valores del heithg print(list(map(lambda x: x["Height"] ,lin_diccionario)))
#Accede a valores de Heithg y los almacena en una variable
valores = list(map(lambda x: x["Height"] , lin_diccionario))
#Funcion que compara hasta encontrar el valor minimo en los valores del heigth
funcion4 = lambda x: list(x.items())[2][1] == min(valores)
#Funcion que compara hasta encontrar el valor maximo en los valores del heigth
funcion5 = lambda x: list(x.items())[2][1] == max(valores)
print("Jugador con la altura minima ")
#Impresion de Datos dle jugador con altura minima
print(list(filter(funcion4, lin_diccionario)))
print("Jugador con la altura maxima")
#Impresion de Datos dle jugador con altura maxima
print(list(filter(funcion5, lin_diccionario)))

#NOTAS
#map para plicar funciones a una lista 
#Usos de las fucniones lambda

'''
Ejemplo para la aplicacion de la funcion lambda que accede 
los items los coge a cada llave de los diccionarios 
y los alamcena en tuplas, items es propio de los diccionarios
funcion1 = lambda x: list(x.items())[3][1]
list(map(funcion, lin_diccionario))
#lin_diccionario = json.loads(lineas[0])
#print(lin_diccionario)

'''
