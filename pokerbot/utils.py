"""
Utilities for poker, such as Cards, Hands, and Scorers. 
"""

# Imports
import numpy as np

# Constants
suits = {
    "h" : "Hearts",
    "c" : "Clubs",
    "d" : "Diamonds",
    "s" : "Spades",
}

ranks = {
    "2" : "Two",
    "3" : "Three",
    "4" : "Four",
    "5" : "Five",
    "6" : "Six",
    "7" : "Seven",
    "8" : "Eight",
    "9" : "Nine",
    "10": "Ten",
    "J" : "Jack",
    "Q" : "Queen",
    "K" : "King",
    "A" : "Ace",
}

# Low-Level Classes
class Card:
    def __init__(self,
                 card : str
                 ) -> None:
        """
        Initialize a poker card. Input string should be of the format RankSuit.

        Examples:
            - Card("4H") == Four of Hearts
            - Card("JC") == Jack of Clubs
            - Card("AS") == Ace of Spades

        Params
        ------
        card : str
            Desired card in RankSuit format
        """
        card_as_list = list(card)
        card_as_list = card_as_list[:2] # Retain only first two values

        # Capture 0th element of list, convert to lowercase, obtain rank
        self._rank = ranks[card_as_list[0].lower()]

        # Capture 1st element of list, convert to lowercase, obtain suit
        self._suit = suits[card_as_list[1].lower()]

    def print_card(self) -> str:
        """
        Returns card as string. 

        Examples:
            - Card("4H") returns "Four of Hearts"
            - Card("JC") returns "Jack of Clubs"
            - Card("AS") returns "Ace of Spades"

        Returns
        -------
        card_string : str
            String representation of current card. 
        """
        return f"{self._rank} of {self._suit}"
        
    
# High-Level Classes
class Hand:
    def __init__(self):
        raise NotImplementedError

