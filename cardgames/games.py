"""
Module containing various card games. 
"""

### Imports ###
import numpy as np
from cardgames.utils import Card, Hand, Deck, ranks, suits, all_ids, \
N_CARDS_PER_DECK

### Constants ###


### Game Classes ###
class GameBase:
    def __init__(self,
                 n_decks : int,
                 ) -> None:
        # Need to think how to best design this for reusability
        self._n_decks = n_decks
        self.deck = Deck(n_decks=n_decks)
        

### Simple Card Game Idea ###
"""
Deck: single deck, shuffled
Rank Valuation: 2 = 2, ..., A = 14
Suit Valuation: Parity
Scoring: points += 10 - |guess - value(card)|
Goal: Obtain the highest score by the time the deck is ran through. 

Each turn is as follows:
    1. Agent makes a guess for the value of the next dealt card.
    2. Card is dealt. 
    3. Score is incremented. 

"""
