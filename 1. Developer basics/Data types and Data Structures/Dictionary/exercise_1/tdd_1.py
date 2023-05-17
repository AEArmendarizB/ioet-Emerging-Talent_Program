import pytest

import exercise_1 


def test__read_text_file():
    file = "/Users/ioet/Documents/ioet-Andres Armendariz/1. Developer basics/Data types and Data Structures/Dictionary/exercise_1/test_file.txt"
    text_expected = "Hola mundo"
    text = exercise_1.read_file(file)
    assert text_expected == text