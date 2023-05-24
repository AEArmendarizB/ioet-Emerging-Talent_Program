
def reverted_expression(expression: str)->list:
    expression_stack:str = []
    for character in expression:
        expression_stack.append(character)
    return expression_stack


def iterate_stack(expression_stack: list)->str:
    expression_inverted = ""
    while len(expression_stack) > 0:
        expression_inverted += expression_stack.pop()
    return expression_inverted
    
# Define the function for inverted a expression
# def inverted_expression(expression: str) -> str:
#     inverted: str = []
#     new_expression: str = ""
#     for character in expression:
#         inverted.append(character)

#     # Iterate throught the stack
#     while len(inverted) > 0:
#         new_expression = new_expression + inverted.pop()

#     return new_expression


# # Request the expression
# expression: str = input("Ingrese una cadena de texto: ")
# print("La cadena invertida es: ")
# print(f"{inverted_expression(expression)}")
