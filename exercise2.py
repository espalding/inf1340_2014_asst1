#!/usr/bin/env python3

"""
    Perform a checksum on a UPC

    Assignment 1, Exercise 2, INF1340 Fall 2014
"""

__author__ = 'Elisabeth Spalding'
__email__ = "elisabeth.spalding@mail.utoronto.ca"

__copyright__ = "2014 Elisabeth Spalding"
__license__ = "MIT License"

__status__ = "Prototype"


def add_list_contents(l):
    """
    Adds the contents of a string list.
    """
    temp_sum = 0
    for ele in l:
        temp_sum += int(ele)
    return temp_sum


def checksum(upc):
    """
    Checks if the digits in a UPC is consistent with checksum.

    :param upc: a 12-digit universal product code
    :return:
        Boolean: True, checksum is correct
        False, otherwise
    :raises:
        TypeError if input is not a strong
        ValueError if string is the wrong length (with error string stating
        how many digits are over or under
    """

    # check type of input
    # raise TypeError if not string
    if type(upc) is not str:
        raise TypeError("Input is not a String")

    # check length of string
    # raise ValueError if not 12
    elif len(upc) is not 12:
        if len(upc) > 12:
            raise ValueError
            ("Length of Input is over by %d digits." % (len(upc)-12))
        if len(upc) < 12:
            raise ValueError
            ("Length of Input is under by %d digits." % (12-len(upc)))

    # generate checksum using the first 11 digits provided
    else:
        # odd_list contains all the odd digits from digit 0 to 11
        # of the given string.
        odd_list = list(upc[0:11:2])
        # even_list contains all the even digits from digit 1 to 11
        # of the given string.
        even_list = list(upc[1:11:2])

        # temporary variable to store the calculated checksum using first
        # 11 digits of given string.
        cksum = 0

        # *********Step1************
        # sum all the elements of odd list.
        # store the sum in cksum temporary variable.
        # multiply the resulted cksum with 3.
        cksum = cksum + add_list_contents(odd_list)
        cksum *= 3

        # ********Step2************
        # sum all the elements of even list.
        # add the sum with the previous result (cksum).
        cksum = cksum + add_list_contents(even_list)

        # *********Step3************
        # take Modulo 10 of resulted cksum.
        cksum %= 10

        # *********Step4************
        # if cksum is not equal to zero then subtract it from 10.
        if cksum != 0:
            cksum = 10-cksum

        # check the calculated cksum against the the twelfth digit of given string.
        # return True if they are equal, False otherwise.
        if int(upc[11]) == cksum:
            return True
        else:
            return False
