"""
Functions to test utils module.
"""

### Imports ###
import pytest
from cardgames.utils import Card, Hand, ranks, suits

### Constants ###
# Generate list of all possible IDs, with corresponding ranks and suits
all_ids = []
matching_ranks = []
matching_suits = []
for rank in ranks.keys():
    for suit in suits.keys():
        all_ids.append(rank + suit) # Add current card ID to all_ids
        matching_ranks.append(rank) # Add corresponding rank to list
        matching_suits.append(suit) # Add corresponding suit to list

class TestCard:
    def test_id(self) -> None:
        for card_id in all_ids:
            card = Card(card_id)
            assert (card.id == card_id)

    def test_rank(self) -> None:
        for i, card_id in enumerate(all_ids):
            card = Card(card_id)
            assert (card.rank == matching_ranks[i])

    def test_suit(self) -> None:
        for i, card_id in enumerate(all_ids):
            card = Card(card_id)
            assert (card.suit == matching_suits[i])

    def test_rank_name(self) -> None:
        for i, card_id in enumerate(all_ids):
            card = Card(card_id)
            assert (card.rank_name == ranks[matching_ranks[i]])

    def test_suit_name(self) -> None:
        for i, card_id in enumerate(all_ids):
            card = Card(card_id)
            assert (card.suit_name == suits[matching_suits[i]])

    def test_card_name(self) -> None:
        for i, card_id in enumerate(all_ids):
            card = Card(card_id)
            rank = ranks[matching_ranks[i]] 
            suit = suits[matching_suits[i]]
            card_name = f"{rank} of {suit}"

            assert (card.card_name == card_name)
