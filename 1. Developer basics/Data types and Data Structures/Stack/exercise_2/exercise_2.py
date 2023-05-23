

def is_a_digit(operands:str, character:str)->str:
    if character.isdigit():
        number = int(character)
        operands.append(number)
    return operands

def evaluate_postfix(operands:str,character:str)->str:
    if not character.isdigit():
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
    return operands

if __name__ == "__main__": 
    expression = input("Ingrese la expresion posfija a ser evaluada: ")
    operands = []
    for character in expression: 
        operands = is_a_digit(operands,character)
        operands = evaluate_postfix (operands,character)
    print ("El valor es: "f"{operands.pop()}")



