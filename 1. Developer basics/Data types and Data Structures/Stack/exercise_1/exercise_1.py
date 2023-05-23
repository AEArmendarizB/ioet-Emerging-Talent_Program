# #EJERCICIO DE VERIFICACION DE PARENTESIS:
# #Escribe una función que tome una cadena que contiene paréntesis, corchetes y llaves, y verifique si los paréntesis están balanceados. 
# #Es decir, que cada paréntesis abierto tenga su correspondiente paréntesis cerrado en el orden correcto. Utiliza una pila para llevar un 
# #seguimiento de los paréntesis abiertos y cierra el último paréntesis abierto si se encuentra un paréntesis cerrado.


def add_character(parentheses: str, grouping_signs:str)->str:
    grouping_signs: str = []
    for character in parentheses:
        if character in ['(','[','{']:
            grouping_signs.append(character)
        else:
            return grouping_signs

def delete_character(parentheses: str, grouping_signs: str)->str:
    for character in parentheses:
        if character in [')',']','}']:
            if not grouping_signs:
                return "La expresion no esta balanceada"
            sign:str =grouping_signs.pop()
            if character == ')' and sign != '(':
                return "La expresion no esta balanceada"
            if character == ']' and sign != '[':
                return "La expresion no esta balanceada"
            if character == '}' and sign != '{':
                return "La expresion no esta balanceada"
            

# #Function por balanced parentheses
# def balanced_grouping_signs(string:str):
   
#     #Define the stack
#     grouping_signs:str = []

#     for character in string:
#         #If the character is a open parentheses add the element to stack
#         if character in ['(','[','{']:
#             grouping_signs.append(character)

#             #If the character is a close parentheses and the stack es empy, the string isn't balanced.
#         elif character in [')',']','}']:
#             if not grouping_signs:
#                 print("La expresion no esta balanceada")

#             #If the stack isn't empy, pop the last element from stack until find the corresponding closing sign 
#             sign = grouping_signs.pop()
#             if character == ')' and sign != '(':
#                 return print("La expresion no esta balanceada")
#             if character == ']' and sign != '[':
#                 return print("La expresion no esta balanceada")
#             if character == '}' and sign != '{':
#                 return print("La expresion no esta balanceada")
#     if len(grouping_signs) == 0:
#         return print("La expresion esta balanceada")
#     else: 
#         return print("La expresion no esta balanceada")
            
# if __name__ == "__main__":
#     #Request a string
#     input_string: str = input("Ingrese la cadena a ser verificada: ")
#     balanced_grouping_signs(input_string)
