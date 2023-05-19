import pytest

import exercise_3

def test__save_grades__return_dictionay__when_inputs_are_dictionary_of_students_and_student():
    students = {"student_1":{"grade_1":0,"grade_2":0,"grade_3":0,"grade_4":0,"grade_5":0},
                "student_2":{"grade_1":0,"grade_2":0,"grade_3":0,"grade_4":0,"grade_5":0}}
    student = "student_1"
    dictionary_expected = {'student_1':{'grade_1':'10','grade_2':'10','grade_3':'10','grade_4':'10','grade_5':'10'},"student_2":{"grade_1":0,"grade_2":0,"grade_3":0,"grade_4":0,"grade_5":0}}
    dictionary = exercise_3.save_grades(students, student)
    assert dictionary_expected == dictionary

def test__save_grades_all_students__return_dictionary__when_input_is_dictionary():
    students = {"student_1":{"grade_1":0,"grade_2":0,"grade_3":0,"grade_4":0,"grade_5":0},
                "student_2":{"grade_1":0,"grade_2":0,"grade_3":0,"grade_4":0,"grade_5":0}}
    dictionary_expected = {"student_1":{"grade_1":'10',"grade_2":'10',"grade_3":'10',"grade_4":'10',"grade_5":'10'},
                                "student_2":{"grade_1":'10',"grade_2":'10',"grade_3":'10',"grade_4":'10',"grade_5":'10'}}
    dictionary = exercise_3.save_grades_all_students(students)
    assert dictionary_expected == dictionary
    