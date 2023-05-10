#EJERCICIO DE EVALUACION DE EXPRESIONES POSFIJAS
#Escribe una función que tome una expresión posfija (notación polaca inversa) y calcule su resultado utilizando una pila para 
#almacenar los operandos. Para evaluar la expresión, recorre cada elemento de la cadena y si es un operando lo apila en la pila, 
#si es un operador lo desapila junto con los dos operandos previos y aplica la operación correspondiente, y apila el resultado de 
#vuelta en la pila.


#Define a function
def evaluate_postfix_expresion(expression: str) ->str:
    operands = []
    number = ""
    for character in expression:
        if character.isdigit():
            number = int(character)
            operands.append(number)
        else:
            operand_2 = operands.pop()
            operand_1 = operands.pop()
            if character == '+':
                operands.append(operand_1+operand_2)
            elif character == '-':
                operands.append(operand_1-operand_2)
            elif character == '*':
                operands.append(operand_1*operand_2)
            elif character == '/':
                operands.append(operand_1/operand_2)    
            number=""
    return operands.pop()

    #Request postfix expression
expression = input("Ingrese la expresion posfija a ser evaluada: ")
print("EL valor es: " f"{evaluate_postfix_expresion(expression)}")


