import pytest

import exercise_2

def test__is_a_digit__return_stack__when_inputs_is_stack():
    character = '2'
    stack = []
    operands_expected=""
    operands = exercise_2.is_a_digit(character,stack)
    assert operands_expected == operands