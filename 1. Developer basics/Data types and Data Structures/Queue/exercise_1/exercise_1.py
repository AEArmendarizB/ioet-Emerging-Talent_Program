#EJERCICIO DE SIMULACION DE UNA COLA DE SUPERMERCADO:
#Escribe un programa que simule el comportamiento de una cola de clientes en un supermercado. Los clientes llegan al supermercado en 
#intervalos aleatorios de tiempo, y cuando llega su turno en la cola, realizan una compra que también toma un tiempo aleatorio. 
#La cola debe ser implementada utilizando una lista y la simulación debe hacerse utilizando el módulo time.


#Import libraries
import random 
import time
from queue import Queue

def add_new_client(supermarket, client):
    time.sleep(random.randint(0, 5))
    supermarket.put(client)  
    #print ("El cliente" f"{client}" "se añadio a la cola")
    return supermarket

# supermarket: int = Queue()              #Declarate a queue and principals variables
# num_iterations: int = 25               #max size of iterations


# #Funtion to add a new client to queue
# def new_client(client: int):
#     time.sleep(random.randint(0, 5))
#     supermarket.put(client)
#     print("El cliente " f"{client}" " se añadio a la cola")

# #Funtion to atend a client and delete from queue
# def atend_client():
#     if supermarket.qsize()>0: 
#         time.sleep(random.randint(0, 5))
#         atend: int  = supermarket.get()
#         print("El cliente  " f"{atend}" " fue atendido")
#         if supermarket.qsize()==0:
#             print("No hay clientes en la cola")

# for i in range(num_iterations):
#     opcion: int = random.randint(1,2)       #determinate a new client or atend the client. If opcion = 1 is a new client else atend the client
#     if opcion == 1:
#         client: int = random.randint(1,20)      #represent each client
#         new_client(client)
#     else:
#         atend_client()