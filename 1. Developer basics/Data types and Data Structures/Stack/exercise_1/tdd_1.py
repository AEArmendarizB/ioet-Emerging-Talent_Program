import pytest

import exercise_1

def test__add_character__return_stack__when__input_is_a_string():
    string = "((()))"
    stack_expected = ['(','(','(']
    stack = exercise_1.add_character(string)
    assert stack_expected == stack