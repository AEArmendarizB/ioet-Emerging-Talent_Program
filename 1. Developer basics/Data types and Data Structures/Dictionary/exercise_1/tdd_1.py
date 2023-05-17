import pytest
from collections import defaultdict

import exercise_1 


def test__read_text_file__return_string__when_input_is_a_path():
    file = "/Users/ioet/Documents/ioet-Andres Armendariz/1. Developer basics/Data types and Data Structures/Dictionary/exercise_1/test_file.txt"
    text_expected = "Hola mundo"
    text = exercise_1.read_file(file)
    assert text_expected == text

def test__split_in_words__return_array__when_input_is_a_string():
    string = "Hola mundo"
    split_expected = ["Hola","mundo"]
    split = exercise_1.split_in_words(string)
    assert split_expected == split

def test__count_words__return_dictionary__when_input_is_a_array():
    split = ["Hola","mundo","Hola","mundo","Hola","mundo"]
    count_expected:dict = {"Hola":3,"mundo":3}
    count = exercise_1.count_words(split)
    assert count_expected == count

def test__show_results_return_array_of_tuples__when_input_is_a_dictionary():
    count = {"Hola":3,"mundo":3}
    result_expected = [("Hola",3),("mundo",3)]
    result = exercise_1.show_results(count)
    assert result_expected == result