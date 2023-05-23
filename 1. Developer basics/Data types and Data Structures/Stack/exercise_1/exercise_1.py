
def add_character(character: str, grouping_signs:str)->str:
    if character in ['(','[','{']:
        grouping_signs.append(character)
    return grouping_signs

def delete_character(character: str, grouping_signs: str)->tuple:
    balanced:bool = True
    if character in [')',']','}']:
        if not grouping_signs:
            balanced = False
        sign:str =grouping_signs.pop()
        if character == ')' and sign != '(':
            balanced = False
        if character == ']' and sign != '[':
            balanced = False
        if character == '}' and sign != '{':
            balanced = False
    return grouping_signs, balanced      
            
if __name__ == "__main__":
    #Request a string
    input_string: str = input("Ingrese la cadena a ser verificada: ")
    grouping_signs:str = []
    for character in input_string:
        grouping_signs = add_character(character, grouping_signs)
        grouping_signs, balanced = delete_character(character, grouping_signs)
        if balanced == False:
            print("La expresion no esta balanceada")
    if len(grouping_signs) == 0 and balanced == True:
        print("La expresion esta balanceada")
