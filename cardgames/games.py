"""
Module containing various card games. 
"""

### Imports ###
import numpy as np
import gymnasium as gym
from gymnasium import spaces

from cardgames.utils import Card, Hand, Deck, ranks

### Constants ###
simple_rank_scores = {
    k : v for k, v in zip(ranks.keys(), range(len(ranks)))
}

### Game Classes ###
class GameBase(gym.Env):
    """Base Game Environment that follows gym interface."""
    def __init__(self, 
                 n_decks : int, 
                 rank_scores : dict,
                 n_actions=None,
                 ) -> None:
        # Constants
        self.low = -1
        self.high = 1

        self.n_decks = n_decks
        self.rank_scores = rank_scores
        
        super().__init__()

        if n_actions is None:
            n_actions = len(rank_scores)

        self.action_space = spaces.Discrete(n_actions)
        self.observation_space = spaces.Discrete(len(rank_scores))

    def normalize(self, val : int) -> float:
        mean = (len(self.rank_scores) - 1) / 2
        return (val - mean) / mean
    
    def reward(self, observation : int, action : int) -> float:
        obs_norm = self.normalize(observation)
        action_norm = self.normalize(action)

        return 1 - abs(obs_norm - action_norm)

    def step(self, action):
        self.card = self.deck.deal()[0]  # Deal a single card and store it
        observation = self.rank_scores[self.card.rank]
        
        terminated = bool(self.deck.n_cards == 0)
        truncated = False  # we do not limit the number of steps here
        reward = self.reward(observation, action)
        info = {}

        return (
            observation,
            reward,
            terminated,
            truncated,
            info,
        )

    def reset(self, seed=None, options=None):
        self.deck = Deck(self.n_decks, seed)
        self.deck.shuffle()
        self.card = self.deck.deal()[0]  # Deal a single card and store it

        observation = self.rank_scores[self.card.rank]
        return observation, {}  # Empty info dict

    def render(self):
        print(f"Dealt {self.card.name}\n")

    def close(self):
        pass
