import pytest

import exercise_2

def test__is_a_digit__return_stack__when_inputs_are_stack_and_character():
    character = '2'
    stack = []
    operands_expected = [2]
    operands = exercise_2.is_a_digit(stack,character)
    assert operands_expected == operands

def test__evaluate_postfix__return_stack__when_inputs_is_stack():
    stack = [2,3]
    operands_expected = ""
    operands = exercise_2.evaluate_postfix(stack)
    assert operands_expected == operands