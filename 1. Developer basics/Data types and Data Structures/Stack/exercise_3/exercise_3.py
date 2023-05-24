
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
    
if __name__ == "__main__":
    expression: str = input("Ingrese una cadena de texto: ")
    expression_stack = reverted_expression(expression)
    print (iterate_stack(expression_stack))

