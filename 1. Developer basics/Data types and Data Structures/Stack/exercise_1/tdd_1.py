import pytest

import exercise_1

def test__add_character__return_stack__when__input_is_a_string():
    character = "("
    grouping_sing = ['(','(']
    stack_expected = ['(','(','(']
    stack = exercise_1.add_character(character, grouping_sing)
    assert stack_expected == stack

def test__delete_character__return_stack_and_boolean__when_input_is_a_stack_and_string():
    character = "}"
    grouping_sing = ['(','(','(']
    stack_deleted_expected = (['(','('], True)
    stack_deleted = exercise_1.delete_character(character, grouping_sing)
    assert stack_deleted_expected == stack_deleted