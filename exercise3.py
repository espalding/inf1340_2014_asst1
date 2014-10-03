#!/usr/bin/env python3

"""
    Decide the winner of a Rock-Paper-Scissors Game.

    Assignment 1, Exercise 3, INF1340 Fall 2014
"""

__author__ = 'Elisabeth Spalding'
__email__ = "elisabeth.spalding@mail.utoronto.ca"

__copyright__ = "2014 Elisabeth Spalding"
__license__ = "MIT License"

__status__ = "Prototype"


def decide_rps(player1, player2):
    """
        Returns the result of Rock-Paper-Scissors game
        played between two players.

        :param:
        player1: input entered by player1
        player2: input entered by player2

        :return:
            Integer:
                0, Game is a Tie.
                1, Player1 wins the game.
                2, Player2 wins the game.

        :raises:
            ValueError: if the input from either player is not valid.
        """

    # Rock-Paper-Scissor list to check if the input is valid.
    rps_list = ['SCISSORS', 'PAPER', 'ROCK']

    # Rock-Paper-Scissor dictionary to determine the winner.
    rps_dict = {('SCISSORS', 'PAPER'): 1,
                ('PAPER', 'SCISSORS'): 2,
                ('PAPER', 'ROCK'): 1,
                ('ROCK', 'PAPER'): 2,
                ('ROCK', 'SCISSORS'): 1,
                ('SCISSORS', 'ROCK'): 2}

    if type(player1) is str and type(player2) is str:
        # change the input values from the players to upper case
        # so that lower case inputs are also valid.
        player1 = player1.upper()
        player2 = player2.upper()

        # check if the players has input the valid values using rps_list.
        if player1 in rps_list and player2 in rps_list:
            # if inputs are same for both players then the game is tie.
            if player1 == player2:
                return 0
            # else create a tuple of input of players
            # to use it as key in rps_dict.
            else:
                tup = (player1, player2)
                return rps_dict.get(tup)
        else:
            raise ValueError("The input values are incorrect.")
    else:
        raise TypeError("The input type is not string.")
