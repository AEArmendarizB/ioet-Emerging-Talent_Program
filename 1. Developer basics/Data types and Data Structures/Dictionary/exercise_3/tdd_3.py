import pytest

import exercise_3

def test__save_grades__return_dictionay__when_inputs_are_dictionary_of_students_array_of_5_grades_and_student():
    grades=[10.0,9.0,10.0,7.0,10.0]
    students = {"student_1":{"grade_1":0,"grade_2":0,"grade_3":0,"grade_4":0,"grade_5":0},
                "student_2":{"grade_1":0,"grade_2":0,"grade_3":0,"grade_4":0,"grade_5":0}}
    student = "student_1"
    dictionary_expected =""
    dictionary = exercise_3.add_grades()
    assert dictionary_expected == dictionary