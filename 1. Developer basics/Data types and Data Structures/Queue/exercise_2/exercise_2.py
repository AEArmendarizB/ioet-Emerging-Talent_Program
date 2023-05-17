#EJERCICIO DE ORDENAMIENTO POR MEZCLA UTILIZANDO COLAS: 
#Escribe Escribe una función que implemente el algoritmo de ordenamiento por mezcla utilizando dos colas. La función debe tomar una 
#lista de números desordenados, y dividirla en dos sub-listas de tamaño aproximadamente igual. Luego, debe ordenar cada sub-lista utilizando 
#la misma función recursivamente, y finalmente mezclar las dos colas resultantes en una sola cola ordenada.


from queue import Queue

#Funtion to separate a string into 2 new strings
def strings(input_string):
    if len(input_string)<=1: 
        return Queue(input_string)

    middle: int = len(input_string)//2
    left_string:int = input_string[:middle]
    right_string: int = input_string[middle:]

    #call to recursive funtion
    left_sorted_string: int = strings(left_string)
    right_sorted_stirng: int = strings(right_string)

    #Join and sort the strings
    outpu_string = Queue()
    while left_sorted_string and right_sorted_stirng:
        if left_sorted_string[0] < right_sorted_stirng[0]:
            outpu_string.put(left_sorted_string.popleft())
        else:
            outpu_string.put(right_sorted_stirng.popleft())
    outpu_string.extend(left_sorted_string)
    outpu_string.extend(right_sorted_stirng)

    return outpu_string

input_string = input("Ingrese una cadena: ")
print(strings(input_string))
