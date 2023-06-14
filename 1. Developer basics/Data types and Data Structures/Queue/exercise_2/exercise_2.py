from queue import Queue

def strings(input_string):
    if len(input_string) <= 1: 
        return Queue(input_string)

    middle = len(input_string) // 2
    left_string = input_string[:middle]
    right_string = input_string[middle:]

    left_sorted_string = strings(left_string)
    right_sorted_stirng = strings(right_string)

    output_string = Queue()
    while not left_sorted_string.empty() and not right_sorted_stirng.empty():
        if left_sorted_string.queue[0] < right_sorted_stirng.queue[0]:
            output_string.put(left_sorted_string.get())
        else:
            output_string.put(right_sorted_stirng.get())
    
    while not left_sorted_string.empty():
        output_string.put(left_sorted_string.get())
    
    while not right_sorted_stirng.empty():
        output_string.put(right_sorted_stirng.get())

    return output_string

# Ejemplo de uso
input_str = "openai"
result_queue = strings(input_str)

# Mostrar el contenido de la cola en la consola
while not result_queue.empty():
    print(result_queue.queue[0])
    result_queue.get()
