
def add_character(character: str, grouping_signs:str)->str:
    if character in ['(','[','{']:
        grouping_signs.append(character)
    return grouping_signs

def delete_character(character: str, grouping_signs: str)->str:
    if character in [')',']','}']:
        if not grouping_signs:
            print( "La expresion no esta balanceada")
        sign:str =grouping_signs.pop()
        if character == ')' and sign != '(':
            print( "La expresion no esta balanceada")
        if character == ']' and sign != '[':
            print( "La expresion no esta balanceada")
        if character == '}' and sign != '{':
            print( "La expresion no esta balanceada")
    return grouping_signs      
            
if __name__ == "__main__":
    #Request a string
    input_string: str = input("Ingrese la cadena a ser verificada: ")
    grouping_signs:str = []
    for character in input_string:
        grouping_signs = add_character(character, grouping_signs)
        grouping_signs = delete_character(character, grouping_signs)
    if len(grouping_signs) == 0:
        print("La expresion esta balanceada")
    else: 
        print("La expresion no esta balanceada")
