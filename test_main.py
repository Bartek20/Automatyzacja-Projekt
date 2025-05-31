# test_calculator.py
import pytest
from main import module, echo
def test_module():
 assert module() == 0
def test_divide():
 assert echo('test') == None
 assert echo('test123') == None
