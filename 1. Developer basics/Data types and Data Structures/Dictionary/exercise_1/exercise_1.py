
#Define the Dictionary
from collections import defaultdict
path:str =  "/Users/ioet/Documents/ioet-Andres Armendariz/1. Developer basics/Data types and Data Structures/Dictionary/exercise_1/file.txt"

#Open and read the file 
def read_file(path:str)->str:
    with open(path) as file:
        text = file.read()
    return text

#Transform all the string in words
def split_in_words(text: str):
    words:str = text.split()
    return words

#iterate and count frecuency words
def count_words(words: str):
    frecuency:dict = defaultdict(int)
    for word in words:
        if word not in frecuency:
            frecuency[word] = 1
        else:
            frecuency[word] += 1
    return frecuency

#Show the results
def show_results(frecuency: dict):
    result:str =""
    for word in frecuency:
        result += (word,frecuency[word])
    return result


print("Las palabras y sus frecuencias son: ")
text:str = read_file(path)
words:str = split_in_words(text)
frecuency = count_words(words)
print(show_results(frecuency))

