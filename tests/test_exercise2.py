import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from exercises.exercise2 import is_odd

def test_number_is_odd():
    number_input = 7
    result = is_odd(number_input)

    assert result is True

def test_number_is_not_odd():
    number_input = 6
    result = is_odd(number_input)

    assert result is False