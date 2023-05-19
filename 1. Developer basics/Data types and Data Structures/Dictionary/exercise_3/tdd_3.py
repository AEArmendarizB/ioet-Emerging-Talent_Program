import pytest

import exercise_3

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

def test__students_average__return_tuple__when_input_is_dictionary_of_students():
    students = {"student_1":{"grade_1":'10',"grade_2":'10',"grade_3":'10',"grade_4":'8',"grade_5":'8'},
                "student_2":{"grade_1":'10',"grade_2":'9',"grade_3":'9',"grade_4":'8',"grade_5":'8'},
                "student_3":{"grade_1":'10',"grade_2":'9',"grade_3":'9',"grade_4":'8',"grade_5":'8'},
                "student_4":{"grade_1":'10',"grade_2":'9',"grade_3":'9',"grade_4":'8',"grade_5":'8'},
                "student_5":{"grade_1":'10',"grade_2":'9',"grade_3":'9',"grade_4":'8',"grade_5":'8'}}
    students_average = {"student_1":0, "student_2":0,"student_3":0,"student_4":0,"student_5":0}
    dictionary_exepcted = ({'student_1':9.2, 'student_2':8.8, 'student_3':8.8, 'student_4':8.8, 'student_5':8.8},8.88)
    dictionary = exercise_3.calculated_students_average(students_average, students)
    assert dictionary_exepcted == dictionary