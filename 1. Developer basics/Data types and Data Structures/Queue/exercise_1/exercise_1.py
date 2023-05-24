#EJERCICIO DE SIMULACION DE UNA COLA DE SUPERMERCADO:
#Escribe un programa que simule el comportamiento de una cola de clientes en un supermercado. Los clientes llegan al supermercado en 
#intervalos aleatorios de tiempo, y cuando llega su turno en la cola, realizan una compra que también toma un tiempo aleatorio. 
#La cola debe ser implementada utilizando una lista y la simulación debe hacerse utilizando el módulo time.


#Import libraries
import random 
import time
from queue import Queue

def add_new_client(supermarket:list, client:int)->list:
    time.sleep(random.randint(0, 5))
    supermarket.put(client)  
    print ("El cliente  "  f"{client}" "  se añadio a la cola")
    return supermarket

def attend_client(supermarket:list)->list:
    if supermarket.qsize() > 0:
        time.sleep(random.randint(0, 5))
        client:int = supermarket.get()
        print ("El cliente  " f"{client}" "  fue atendido")
        return supermarket
    if supermarket.qsize() == 0:
        print("No hay clientes en la cola")
        return supermarket

if __name__ == "__main__":
    supermarket:int = Queue()
    num_iterations = 25
for i in range(num_iterations):
    opcion:int = random.randint(1, 2)
    if opcion == 1:
        supermarket = add_new_client(supermarket, random.randint(1, 100))
    else:
        supermarket = attend_client(supermarket)
