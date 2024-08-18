"""
Simulate and compare performance of RL agents vs statistical methods 
for a simple card game. 
"""

### Imports ###
import numpy as np
from stable_baselines3 import DQN

from cardgames import games

### CONSTANTS ###
n_decks = 1
n_runs = int(1e4 / n_decks)
total_timesteps = int(1e5)

### Functions ###
def simulate_run(name, action_func):
    env = games.GameSimulator(n_decks, games.simple_rank_scores)
    print(f"Using {name} method:")
    
    rewards = np.zeros((n_runs,))
    for i in range(n_runs):
        rewards[i] = sum(env.simulate_run(action_func))

    print(f"Mean reward per episode after {n_runs} runs:" 
          f" {rewards.mean() :.2f}\n")

def train_rl():
    env = games.GameBase(n_decks, games.simple_rank_scores)

    model = DQN("MlpPolicy", env, verbose=1, seed=0, exploration_final_eps=0)
    model.learn(total_timesteps=total_timesteps)

def main():
    env = games.GameSimulator(n_decks, games.simple_rank_scores)
    stat_methods = {
        "random"        : env.random,
        "mean score"    : env.mean_observation,
        "expected score": env.expected_observation, 
    }

    for name, func in stat_methods.items():
        simulate_run(name, func)

    train_rl()
        
if __name__ == "__main__":
    main()
