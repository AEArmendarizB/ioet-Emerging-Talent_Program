
#Register all the grades for one student
def save_grades(students:dict, student:dict)->dict:
    num:int  = 1
    for num_grade in students[student]:
        grade:float = input("Nota "f"{num}: ")
        students[student][num_grade] = grade
        num +=1
    return students

#register grades for all the students
def save_grades_all_students(students: dict)->dict:
    num:int = 1 
    for number_student in students:
        print("Ingrese las notas del estudiante " f"{num} ")
        save_grades(students, number_student)
        num+=1
    return students

def calculated_students_average(students_average: dict, students:dict):
    class_average:float = 0.0 
    for number_student in students_average:
        students_average[number_student] = (float(students[number_student]['grade_1'])+float(students[number_student]['grade_2'])+
                                            float(students[number_student]['grade_3'])+float(students[number_student]['grade_4'])+
                                            float(students[number_student]['grade_5']))/5
        class_average += students_average[number_student]
    class_average = class_average/5
    return (students_average, class_average)



if __name__ == '__main__':
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
    
    students:dict = save_grades_all_students(students)
    students_average, average:float = calculated_students_average(students_average, students)

  #Show results
    print("Los promedios de los estudiantes son: ")
    for number_student in students_average:
        print(f"{number_student}" "= " f"{students_average[number_student]}")
    print("El promedio general de la clase es: " f"{average}")
