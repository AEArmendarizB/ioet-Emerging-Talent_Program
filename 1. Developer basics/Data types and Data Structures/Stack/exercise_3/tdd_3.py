import pytest 

import exercise_3

def test__reverted_expression__return_string__when_inputs_is_string():
    string = "Hola"
    expression_expected = ""
    expression = reverted_expression(string)
    assert expression_expected == expression