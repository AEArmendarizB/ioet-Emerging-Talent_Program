


#Check the original measure exist in the dictionary
def check_measure(relation:dict,measure:str)->bool:
    if measure not in relation:
        return False
    

#Evaluate boolean
def evaluate_boolean(boolean:bool):
    if boolean == False:
        print("La unidad de medida ingresada no se acepta")

#Define dictionary
relations = {
    "km":{"hm":100, "m":1000, "dm":10000, "cm":100000, "mm":1000000, "ft":3280.84, "in":39370.1},
    "hm":{"km":0.1, "m":100, "dm":1000, "cm":10000, "mm":100000, "ft":328.084, "in":3937.01},
    "m":{"km":0.001, "hm":0.01, "dm":10, "cm":100, "mm":1000, "ft":3.28084, "in":39.3701},
    "dm":{"km":0.0001, "hm":0.001, "m":0.1, "cm":10, "mm":100, "ft":0.328084, "in":3.93701},
    "cm":{"km":0.00001, "hm":0.0001, "m":0.01, "dm":0.1, "mm":10, "ft":0.0328084, "in":0.393701},
    "mm":{"km":0.000001, "hm":0.00001, "m":0.001, "dm":0.01, "cm":0.1, "ft":0.00328084, "in":0.0393701},
    "ft":{"km":0.0003048000097536, "hm":0.003048000097536, "m":0.3048000097536, "dm":3.048000097536, "cm":30.48000097536, "mm":304.8000097536, "in":12.000000383999999798},
    "in":{"km":0.0000254, "hm":0.000254, "m":0.0254, "dm":0.254, "cm":2.54, "mm":25.4, "ft":0.0833333},
}

#Request information to the client about the original value and measure
input: str = input("Ingrese el valor y la unidad de medida separada por un espacio: ")
input: str = input.split()
value: float = float(input[0])
measure: str =input[1]

axuiliar = check_measure(relations, measure)
#Check the measure exist in the dictionary
if measure not in relations:
    print("La unidad de medida ingresada no se acepta")
else:
#If the measure exist do the conversions with all the respective dictionary
    print("Las conversiones posibles son: ")
    value_conversion(relations,value,measure)
