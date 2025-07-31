import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from exercises.exercise1 import contains_consecutive

def test_array_does_not_contain_consecutive_identical_numbers():
    array_of_numbers = [7, 1, 7]
    number_to_find = 7
    result = contains_consecutive(array_of_numbers, number_to_find)

    assert result is False

def test_array_does_contain_consecutive_identical_numbers():
    array_of_numbers = [1, 7, 7]
    number_to_find = 7
    result = contains_consecutive(array_of_numbers, number_to_find)

    assert result is True