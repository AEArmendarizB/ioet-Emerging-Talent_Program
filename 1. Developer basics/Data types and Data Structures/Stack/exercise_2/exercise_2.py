
# #Define a function
# def evaluate_postfix_expresion(expression: str) ->str:
#     operands = []
#     number = ""
#     for character in expression:
#         if character.isdigit():
#             number = int(character)
#             operands.append(number)
#         else:
#             operand_2 = operands.pop()
#             operand_1 = operands.pop()
#             if character == '+':
#                 operands.append(operand_1+operand_2)
#             elif character == '-':
#                 operands.append(operand_1-operand_2)
#             elif character == '*':
#                 operands.append(operand_1*operand_2)
#             elif character == '/':
#                 operands.append(operand_1/operand_2)    
#             number=""
#     return operands.pop()

#     #Request postfix expression
# expression = input("Ingrese la expresion posfija a ser evaluada: ")
# print("EL valor es: " f"{evaluate_postfix_expresion(expression)}")


