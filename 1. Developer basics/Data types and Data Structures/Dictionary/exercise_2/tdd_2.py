import pytest

import exercise_2

dictionary = {"km":{"m":1000,"cm":10000,"mm":10000}}

def test__value_conversion__return_a_string__when_inputs_are_dictionary_value_and_measure(dictionary):
    value = float(25)
    measure = "km"
    value_expected = ""
    value = exercise_2.value_conversion(dictionary, measure,value)
    assert value_expected == value