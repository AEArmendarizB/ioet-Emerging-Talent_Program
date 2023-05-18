import pytest

import exercise_2



def test__value_conversion__return_a_string__when_inputs_are_dictionary_value_and_measure():
    input_value = float(25)
    measure = "km"
    value_expected = [25000.0,250000.0,25000000.0]
    dictionary = {"km": {"m": 1000, "cm": 10000, "mm": 1000000}}
    value = exercise_2.value_conversion(dictionary, input_value, measure)
    assert value_expected == value

def test__check_measure__return_a_bool__when_inputs_are_dictionary_and_measure():
    measure = "km"
    dictionary = {"km": {"m": 1000, "cm": 10000, "mm": 1000000}}
    boolean_expected = None
    boolean = exercise_2.check_measure(dictionary,measure)
    assert boolean_expected == boolean
