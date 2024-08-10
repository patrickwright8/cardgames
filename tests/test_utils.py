"""
Functions to test utils module.
"""

### Imports ###
import pytest
from cardgames.utils import Card, Hand, ranks, suits, all_ids

### Constants ###
# Generate list of ranks and suits corresopnding to all_ids list
matching_ranks = []
matching_suits = []
for rank in ranks.keys():
    for suit in suits.keys():
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

            assert (card.name == card_name)

class TestHand:
    def test_ids(self):
        """
        Initialize Hand with n (default = 10) decks' worth of cards, then 
        assert that Hand ids match deck ids. 
        """
        n_decks = 10
        ids = all_ids * n_decks
        cards = [Card(id) for id in ids]
        hand = Hand(*cards)

        for count, id in enumerate(hand.ids):
            assert (ids[count] == id)

    def test_add_cards(self):
        """
        Add Cards one-by-one to Hand, and assert that both:
            - The new Card is in the Hand (by id)
            - All previously-added cards are in the Hand (by id)
        """
        hand = Hand()
        for count, id in enumerate(all_ids):
            hand.add_cards(Card(id))

            assert (id in hand.ids)

            prev_ids = all_ids[:count]
            for prev_id in prev_ids:
                assert (prev_id in hand.ids)

    def test_remove_cards(self):
        """
        Fill Hand with one deck's worth of Cards, then remove Cards one-by-one 
        and assert that both:
            - The new Card is not in the Hand (by id)
            - All previously-removed Cards are not in the Hand (by id)
        """
        all_cards = [Card(id) for id in all_ids]
        hand = Hand(*all_cards)

        for count, id in enumerate(all_ids):
            hand.remove_cards(Card(id))
            assert (id not in hand.ids)

            prev_ids = all_ids[:count]
            for prev_id in prev_ids:
                assert (prev_id not in hand.ids)

    def test_remove_by_id(self):
        """
        Fill Hand with one deck's worth of Cards, then remove Cards one-by-one
        by id and assert that both:
            - The new id is not in the Hand
            - All previously-removed ids are not in the Hand
        """
        all_cards = [Card(id) for id in all_ids]
        hand = Hand(*all_cards)

        for count, id in enumerate(all_ids):
            hand.remove_by_id(id)
            assert (id not in hand.ids)

            prev_ids = all_ids[:count]
            for prev_id in prev_ids:
                assert (prev_id not in hand.ids)

if __name__ == "__main__":
    pytest.main()
