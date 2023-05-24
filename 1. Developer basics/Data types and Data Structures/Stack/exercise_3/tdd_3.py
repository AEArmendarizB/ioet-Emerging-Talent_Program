import pytest 

import exercise_3

def test__reverted_expression__return_string__when_inputs_is_stack():
    string = "Hola"
    expression_expected = ['H','o','l','a']
    expression = exercise_3.reverted_expression(string)
    assert expression_expected == expression