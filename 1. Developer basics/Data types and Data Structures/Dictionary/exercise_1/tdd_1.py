import pytest
from collections import defaultdict

import exercise_1 


def test__read_text_file():
    file = "/Users/ioet/Documents/ioet-Andres Armendariz/1. Developer basics/Data types and Data Structures/Dictionary/exercise_1/test_file.txt"
    text_expected = "Hola mundo"
    text = exercise_1.read_file(file)
    assert text_expected == text

def test__split_in_words():
    string = "Hola mundo"
    split_expected = ["Hola","mundo"]
    split = exercise_1.split_in_words(string)
    assert split_expected == split

def test__count_words():
    split = ["Hola","mundo","Hola","mundo","Hola","mundo"]
    count_expected:dict = {"Hola":3,"mundo":3}
    count = exercise_1.count_words(split)
    assert count_expected == count

def test__show_results():
    count = {"Hola":3,"mundo":3}
    result_expected = "mundo", 3
    result = exercise_1.show_results(count)
    assert result_expected == result