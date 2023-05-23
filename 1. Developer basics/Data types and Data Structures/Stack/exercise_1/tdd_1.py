import pytest

import exercise_1

def test__add_character__return_stack__when__input_is_a_string():
    string = "((([({{()}})])))"
    stack_expected = ['(','(','(','[','(','{','{','(']
    stack = exercise_1.add_character(string, string)
    assert stack_expected == stack

def test__delete_character__return_stack__when_input_is_a_stack_and_string():
    string = "((([({{()}})])))"
    stack = ['(','(','(','[','(','{','{','(']
    stack_deleted_expected = []
    stack_deleted = exercise_1.delete_character(string, stack)
    assert stack_deleted_expected == stack_deleted