import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from exercises.exercise3 import find_largest_number

def test_find_largest_number_in_array():
    array_of_numbers = [20, 50, 30, 100, 1, 99]
    result = find_largest_number(array_of_numbers)
    
    assert result == 100