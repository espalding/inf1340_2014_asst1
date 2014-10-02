#!/usr/bin/env python3

""" Assignment 1, Exercise 1, INF1340, Fall, 2014. Grade to gpa conversion

This module contains one function grade_to_gpa. It can be passed a parameter
that is an integer (0-100) or a letter grade (A+, A, A-, B+, B, B-, or FZ). All
other inputs will result in an error.

Example:
    $ python exercise1.py

"""

__author__ = 'Elisabeth Spalding'
__email__ = "elisabeth.spalding@mail.utoronto.ca"

__copyright__ = "2014 Elisabeth Spalding"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line

#letter_to_gpa is a dictionary used to map Letter grades with GPA.
letter_to_gpa = {'A+':4.0, 'A':4.0, 'A-':3.7, 'B+':3.3, 'B': 3.0, 'B-': 2.7, 'FZ' : 0.0}
#numeric_to_gpa is a dictionary used to map Numeric grades with GPA.
numeric_to_gpa = {90: 4.0, 85: 4.0, 80: 3.7, 77: 3.3, 73: 3.0, 70: 2.7, 0: 0.0}

def grade_to_gpa(grade):
    """
    Returns the UofT Graduate GPA for a given grade.

    :param:
        grade (integer or string): Grade to be converted
        If integer, accepted values are 0-100.
        If string, accepted values are A+, A, A-, B+, B, B-, FZ

    :return:
        float: The equivalent GPA
        Value is 0.0-4.0

    :raises:
        TypeError if parameter is not a string or integer
        ValueError if parameter is out of range
    """
    #check if grade is a string and is present in keys of dictionary letter_to_gpa.
    if type(grade) is str:
        if grade in letter_to_gpa.keys():
            return letter_to_gpa.get(grade)
        else:
            raise ValueError("Value is out of range")


    #check if grade is a integer and is in the range 0 to 100.
    elif type(grade) is int:
        if grade in range(0,101,1):
            # Sort the keys of dictionary numeric_to_gpa in descending order.
            # compare the input numeric grade with the sorted keys one by one.
            # if the input numeric grade is greater than or equal to current key then return the relevant gpa.
            for i in sorted(numeric_to_gpa.keys(),reverse=True):
                if(grade>=i):
                    return numeric_to_gpa.get(i)
        else:
                raise ValueError("Value is out of range")
    else:
        raise TypeError("Invalid type passed as parameter")
