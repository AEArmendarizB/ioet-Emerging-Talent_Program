#EJERCICIO DE CONTEO DE PALABRAS 
#Escribe un programa que lea un archivo de texto y cuente la cantidad de veces que aparece cada 
#palabra en el archivo. Luego, almacena los resultados en un diccionario y muestra los pares palabra-frecuencia en orden alfabético.

#Define the Dictionary
from collections import defaultdict
frecuency:dict = defaultdict(int)

#Open and read the file ---- IMPORTANT: change the file path 
with open("/Users/ioet/Documents/ioet-Andres Armendariz/1. Developer basics/Data types and Data Structures/Dictionary/file.txt") as file:
    text = file.read()

#Transform all the string in words
words:str = text.split()

#iterate and count frecuency words
for word in words:
    if word not in frecuency:
        frecuency[word] = 1
    else:
        frecuency[word] += 1

#Show the results
print("Las palabras y sus frecuencias son: ")
for word in frecuency:
    print(word,frecuency[word])
