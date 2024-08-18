"""
Functions to test games module.
"""

### Imports ###
import numpy as np
import pytest
from stable_baselines3.common.env_checker import check_env

from cardgames.games import GameBase, GameSimulator, simple_rank_scores
from cardgames.utils import Card, Hand, N_CARDS_PER_DECK


### Test Classes ###
class TestGameBase:
    def test_env(self):
        env = GameBase(n_decks=1, rank_scores=simple_rank_scores)
        check_env(env)

    def test_normalize_action(self):
        env = GameBase(n_decks=1, rank_scores=simple_rank_scores)
        actions = range(env.action_space.n)

        assert (env.normalize_action(actions[0]) == -1) # Bound for min action
        assert (env.normalize_action(actions[-1]) == 1) # Bound for max action
        
        for action in actions:
            assert ( -1 <= env.normalize_action(action) <= 1 )

    def test_normalize_observation(self):
        env = GameBase(n_decks=1, rank_scores=simple_rank_scores)
        observations = range(env.observation_space.n)

        assert (env.normalize_action(observations[0]) == -1) # Bound for min 
        assert (env.normalize_action(observations[-1]) == 1) # Bound for max 
        
        for observation in observations:
            assert ( -1 <= env.normalize_action(observation) <= 1 )

    def test_reward(self):
        env = GameBase(n_decks=1, rank_scores=simple_rank_scores)
        observations = range(env.observation_space.n)
        actions = range(env.action_space.n)
        mean_observation = np.mean(observations)
        mean_action = np.mean(actions)

        # Test case where action == observation
        for action in actions:
            assert ( env.reward(action, action) == 1 )  # Max reward

        # Test cases with minimum reward
        assert ( env.reward(max(observations), min(actions)) == 0 )
        assert ( env.reward(min(observations), max(actions)) == 0 )

        # Test cases with half reward
        assert ( env.reward(mean_observation, max(actions)) == 0.5)
        assert ( env.reward(mean_observation, min(actions)) == 0.5)
        assert ( env.reward(min(observations), mean_action) == 0.5)
        assert ( env.reward(max(observations), mean_action) == 0.5)

        for observation in observations:
            for action in actions:
                calc_reward = 1 - abs(observation - action) / 2
                reward = env.reward(observation, action)

                assert ( calc_reward == calc_reward )
                assert ( 0 <= reward <= 1)

    def test_reset(self):
        n_decks = 1
        env = GameBase(n_decks=n_decks, rank_scores=simple_rank_scores)
        env.reset()

        assert ( env.deck.n_cards == n_decks * N_CARDS_PER_DECK )

    def test_step(self):
        env = GameBase(n_decks=1, rank_scores=simple_rank_scores)
        env.reset()

        terminated = False
        while not terminated:
            next_score = env.rank_scores[env.deck.cards[0].rank]
            results = env.step(next_score)

            observation = results[0]
            reward = results[1]
            terminated = results[2]

            assert ( observation == next_score )
            assert ( reward == 1 )  # Max reward

class TestGameSimulator:
    def test_observation_distribution(self):
        env = GameSimulator(1, simple_rank_scores)
        env.reset()
        mean_observation = (env.observation_space.n - 1) / 2

        manual_ranks = [card.rank for card in env.deck.cards]
        manual_observations = [env.rank_scores[rank] for rank in manual_ranks]

        assert np.all( env.observation_distribution() == manual_observations )
        assert ( np.mean(env.observation_distribution()) == mean_observation )

    def test_random(self):
        env = GameSimulator(1, simple_rank_scores)
        env.reset()
        max_val = env.observation_space.n - 1
        min_val = 0
        
        n_tries = 100
        for i in range(n_tries):
            val = env.random()
            assert ( min_val <= val <= max_val )

    def test_expected_observation(self):
        env = GameSimulator(1, simple_rank_scores)
        env.reset()
        expected_mean = (env.observation_space.n - 1) / 2

        assert ( expected_mean == env.mean_observation() )

    def test_expected_observation(self):
        test_card = Card("8C")
        manual_exp_observation = simple_rank_scores[test_card.rank]
        
        env = GameSimulator(1, simple_rank_scores)
        env.deck = Hand(test_card)

        assert ( env.expected_observation() == manual_exp_observation )

    def test_simulate_run(self):
        env = GameSimulator(1, simple_rank_scores)
        mean_observation = 6
        
        expected_rewards = 0
        for score in simple_rank_scores.values():
            norm_score = env.normalize_action(score)
            norm_mean_obs = env.normalize_observation(mean_observation)
            
            expected_rewards += 4 * (1 - abs(norm_score - \
                                             norm_mean_obs) / 2 )
        
        rewards = env.simulate_run(env.mean_observation)

        assert np.isclose(np.sum(rewards), expected_rewards)

if __name__ == "__main__":
    pytest.main()
