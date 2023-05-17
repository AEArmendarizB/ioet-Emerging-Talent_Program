#EJERCICIO DE REGISTRO DE NOTAS:
#Escribe un programa que permita registrar las notas de varios estudiantes y luego calcule el promedio de notas de cada estudiante 
#y el promedio general de la clase utilizando un diccionario para almacenar los datos.


#Define dictionary for grades
students = {
    "student_1":{"grade_1":0, "grade_2":0, "grade_3":0, "grade_4":0, "grade_5":0},
    "student_2":{"grade_1":0, "grade_2":0, "grade_3":0, "grade_4":0, "grade_5":0},
    "student_3":{"grade_1":0, "grade_2":0, "grade_3":0, "grade_4":0, "grade_5":0},
    "student_4":{"grade_1":0, "grade_2":0, "grade_3":0, "grade_4":0, "grade_5":0},
    "student_5":{"grade_1":0, "grade_2":0, "grade_3":0, "grade_4":0, "grade_5":0}
}

#Define directory for averages
students_average = {
    "student_1":0,
    "student_2":0,
    "student_3":0,
    "student_4":0,
    "student_5":0
}

num_aux_student: int = 1     #Define an auxilar for first FOR 
num_aux_grade: float = 1       #Define an auxilar for second FOR 
class_average: float = 0       #Define a variable for class average

#Register all the grades for all the students
for number_student in students:
    print("Ingrese las notas del estudiante " f"{num_aux_student} ")
    for number_grade in students[number_student]:
        grade: float = input("Nota " f"{num_aux_grade} :")
        grade = float(grade)
        students[number_student][number_grade] = grade
        num_aux_grade=num_aux_grade+1
    num_aux_student=num_aux_student+1
    num_aux_grade = 1

#Calculate the average for each student and the class average
for number_student in students_average:
    students_average[number_student]=(students[number_student]["grade_1"]+students[number_student]["grade_2"]+students[number_student]["grade_3"]+students[number_student]["grade_4"]+students[number_student]["grade_5"])/5
    class_average = class_average + students_average[number_student]
class_average = class_average/5

#Show results
print("Los promedios de los estudiantes son: ")
for number_student in students_average:
    print(f"{number_student}" "= " f"{students_average[number_student]}")
print("El promedio general de la clase es: " f"{class_average}")
