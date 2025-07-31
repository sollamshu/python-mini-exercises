import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from exercises.exercise4 import sort_numbers_ascending

def test_sort_numbers_ascending_general_case():
    array_of_numbers = [20, 50, 30, 100, 1, 99]
    result = sort_numbers_ascending(array_of_numbers)
    
    assert result == [1, 20, 30, 50, 99, 100]