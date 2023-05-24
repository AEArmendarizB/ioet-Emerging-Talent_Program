import pytest 

import exercise_3

def test__reverted_expression__return_stack__when_inputs_is_string():
    string = "Hola"
    expression_expected = ['H','o','l','a']
    expression = exercise_3.reverted_expression(string)
    assert expression_expected == expression

def test__iterate_stack__return_string__when_inputs_is_stack():
    stack = ['H','o','l','a']
    expression_inverted_expected = "aloH"
    expression_inverted = exercise_3.iterate_stack(stack)
    assert expression_inverted_expected == expression_inverted
