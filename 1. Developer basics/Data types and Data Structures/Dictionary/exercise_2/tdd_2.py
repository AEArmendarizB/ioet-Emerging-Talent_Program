import pytest

import exercise_2



def test__value_conversion__return_a_string__when_inputs_are_dictionary_value_and_measure():
    input_value = float(25)
    measure = "km"
    value_expected = [25000, 250000, 2500000]
    dictionary = {"km": {"m": 1000, "cm": 10000, "mm": 1000000}}
    value = exercise_2.value_conversion(dictionary, input_value, measure)
    assert value_expected == value