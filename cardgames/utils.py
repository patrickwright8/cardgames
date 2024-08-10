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

all_ids = [
    rank + suit
    for rank in ranks.keys()
    for suit in suits.keys()
]

### Low-Level Classes ###
class Card:
    def __init__(self,
                 card : str
                 ) -> None:
        """
        Initialize a Card. Input string should be of the format RankSuit.

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
        """
        Initialize a Hand. Input args must be Cards.

        Examples:
            - `Hand(Card("4H"), Card("8C"), Card("AS"))` initializes a Hand 
              containing Four of Hearts, Eight of Clubs, and Ace of Spades.

        Params
        ------
        *args : Card
            Variable number of Cards, where each Card is input in the format
            `Card("RankSuit")`
        """
        self.cards = [arg for arg in args]
        ids = self.ids  # Generate ids to make sure args are Cards
    
    # Getter properties
    @property
    def ids(self) -> list[str]:
        """
        Alphanumeric IDs associated with each card.
        """
        return [card.id for card in self.cards]
     
    # Public methods
    def add_cards(self,
                  *args : Card
                  ) -> None:
        for arg in args:
            self.cards.append(arg)

    def remove_cards(self,
                     *args : Card
                     ) -> None:
        for arg in args:
            ix = self.ids.index(arg.id)
            self.cards.pop(ix)

    def remove_by_id(self,
                     *args : str
                     ) -> None:
        for arg in args:
            ix = self.ids.index(arg)
            self.cards.pop(ix)

    def print_cardnames(self) -> None:
        names = [ card.name for card in self.cards ]
        string = ", ".join(names)
        print(string)

    def print_ids(self) -> None:
        ids = self.ids
        string = ", ".join(ids)
        print(string)

class Deck(Hand):
    def __init__(self,
                 n_decks=1,
                 ) -> None:
        """
        Initialize a Deck containing `n_decks * 52` Cards. 

        Params
        ------
        n_decks : int (default = 1)
            Number of decks to initialize with. Each of the 52 Cards will have
            `n_decks` occurrences in the Deck. 
        """
        all_cards = [Card(id) for id in all_ids] * n_decks

        super().__init__(*all_cards)

        self._rng = np.random.default_rng()

    def shuffle(self) -> None:
        """
        Shuffles card deck.
        """
        self._rng.shuffle(self.cards)

    def deal(self,
             n : int,
             ) -> list[Card]:
        """
        Deals `n` Cards from top of the deck (starting at 0th index). 
        Removes the cards from the Deck. 

        Params
        ------
        n : int
            Number of cards to be dealt        

        Returns
        -------
        cards : list[Card]
            Cards that were dealt
        """
        if n > len(self.cards):
            raise ValueError("Cannot deal more cards than Deck contains.")

        cards = self.cards[:n]
        self.remove_cards(*cards)

        return cards


