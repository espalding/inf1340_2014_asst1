#!/usr/bin/env python3

""" Module to test exercise2.py """

__author__ = 'Elisabeth Spalding'
__email__ = "elisabeth.spalding@mail.utoronto.ca"

__copyright__ = "2014 Elisabeth Spalding"
__license__ = "MIT License"

__status__ = "Prototype"


# imports one per line

import pytest
from exercise2 import checksum


def test_checksum():
    """
    Inputs that are the correct format and length.
    """
    assert checksum("786936224306") is True
    assert checksum("085392132225") is True
    assert checksum("717951000841") is False
    # other tests


def test_input():
    """
    Inputs that are the incorrect format.
    """
    with pytest.raises(TypeError):
        checksum(1.0)
        checksum(786936224306)


def text_str_len():
    """
    Inputs that are the incorrect length.
    """
    with pytest.raises(ValueError):
        checksum("1")
        checksum("1234567890")
        checksum("123456789")
        checksum("12345678912345")
