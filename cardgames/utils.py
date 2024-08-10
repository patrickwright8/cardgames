"""
Utilities for card games, such as Cards, Hands, and Decks. 
"""

### Imports ###
import numpy as np

### Constants ###
suits = {
    "C" : "Clubs",
    "D" : "Diamonds",
    "H" : "Hearts",
    "S" : "Spades",
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

### Low-Level Classes ###
class Card:
    """
    Class attributes:
    -----------------
    Card.id : str
        Alphanumeric identifier for card

        Examples:
        - Card("4H").id == "4H"
        - Card("JC").id == "JC"
        - Card("AS").id == "AS"

    Card.name : str
        Common name for card

        Examples:
        - Card("4H").name == "Four of Hearts"
        - Card("JC").name == "Jack of Clubs"
        - Card("AS").name == "Ace of Spades"
    """
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
        input_as_list = list(card)

        # Capture 0th up to 2nd-to-last element as str
        # Store as rank
        # Rank is captured this way to support 2-digit '10' rank
        self.rank = "".join(input_as_list[0:-1])
        # Capture last element of list for suit
        self.suit = "".join(input_as_list[-1])
        
        # Generate rank name and suit name
        self.rank_name = ranks[self.rank]
        self.suit_name = suits[self.suit]

        # Generate card name and ID
        self.name = f"{self.rank_name} of {self.suit_name}"
        self.id = self.rank + self.suit

        
### High-Level Classes ###
class Hand:
    def __init__(self,
                 *args : Card
                 ) -> None:
        self.cards = {}
        for arg in args:
            self.cards[arg.id] = arg
    
    # Define getter/setters for ids/cards because these are dynamic
    def get_ids(self) -> list[str]:
        ids = self.cards.keys()
        return list(ids)
    
    def get_cards(self) -> list[Card]:
        cards = self.cards.values()
        return list(cards)
     
    # Public methods
    def add_cards(self,
                  *args : Card
                  ) -> None:
        for arg in args:
            self.cards[arg.id] = arg

    def remove_cards(self,
                     *args : Card
                     ) -> None:
        for arg in args:
            self.cards.pop(arg.id)

    def remove_by_id(self,
                     *args : str
                     ) -> None:
        for id in args:
            self.cards.pop(id)

    def print_cardnames(self) -> None:
        names = [ card.name for card in self.cards ]
        string = ", ".join(names)
        print(string)

    def print_ids(self) -> None:
        ids = self.get_ids()
        string = ", ".join(ids)
        print(string)
