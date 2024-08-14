"""
Functions to test games module.
"""

### Imports ###
import numpy as np
import pytest
from stable_baselines3.common.env_checker import check_env

from cardgames.games import GameBase, simple_rank_scores


### Test Classes ###
class TestGameBase:
    def test_env(self):
        env = GameBase(n_decks=1, rank_scores=simple_rank_scores)
        check_env(env)

    def test_normalize(self):
        env = GameBase(n_decks=1, rank_scores=simple_rank_scores)
        rank_vals = list(simple_rank_scores.values())
        highest = max(rank_vals)
        lowest = min(rank_vals)
        mean = (highest + lowest) / 2

        assert ( np.isclose(env.normalize(highest), 1) )
        assert ( np.isclose(env.normalize(lowest), -1) )
        assert ( np.isclose(env.normalize(mean),  0) )

if __name__ == "__main__":
    pytest.main()
