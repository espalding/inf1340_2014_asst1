#!/usr/bin/env python3

""" Module to test exercise3.py """

__author__ = 'Elisabeth Spalding'
__email__ = "elisabeth.spalding@mail.utoronto.ca"

__copyright__ = "2014 Elisabeth Spalding"
__license__ = "MIT License"

__status__ = "Prototype"


import pytest
from exercise3 import decide_rps


def test_decide_rps():
    """
    Inputs that are the correct format and length
    """
    assert decide_rps("Rock", "Paper") == 2
    assert decide_rps("Scissors", "Scissors") == 0
    assert decide_rps("Rock", "Scissors") == 1
    assert decide_rps("rock", "rock") == 0


def test_value_decide_rps():
    with pytest.raises(ValueError):
        decide_rps("RCK", "Paper")


def test_type_decide_rps():
    with pytest.raises(TypeError):
        decide_rps(14, 25.4)
