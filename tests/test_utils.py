"""
Functions to test utils module.
"""

### Imports ###
import pytest
from cardgames.utils import Card, Hand, Deck, ranks, suits, all_ids, \
    N_CARDS_PER_DECK

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

class TestDeck:
    def test_shuffle(self):
        """
        Initialize Deck containing `n_decks * N_CARDS_PER_DECK` Cards, then
        shuffle. Assert that each id occurs in Deck exactly `n_decks` times. 
        """
        n_decks = 10
        deck = Deck(n_decks=n_decks)
        deck.shuffle()
        deck_ids = [card.id for card in deck.cards]

        for id in all_ids:
            assert (deck_ids.count(id) == n_decks)

    def test_deal(self):
        """
        Initialize Deck, then deal Cards one-by-one.

        Assert that each dealt Card matches the id from all_ids, and the Card 
        is not in the Deck after being dealt. 
        """
        deck = Deck()

        for id in all_ids:
            card = deck.deal(1)[0]  # Select 0th dealt Card

            assert (card.id == id)
            assert (card.id not in deck.ids)

if __name__ == "__main__":
    pytest.main()
