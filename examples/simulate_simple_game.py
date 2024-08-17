"""
Simulate and compare performance of RL agents vs statistical methods 
for a simple card game. 
"""

### Imports ###
import numpy as np
import json
from stable_baselines3 import DQN, PPO, A2C

from cardgames import games

### CONSTANTS ###
n_decks = 1
n_runs = int(1e5)

### Functions ###
def simulate_run(env : games.GameSimulator, name, action_func):
    print(f"Using {name} method:")
    
    rewards = np.zeros((n_runs,))
    for i in range(n_runs):
        rewards[i] = sum(env.simulate_run(action_func))

    print(f"Mean reward after {n_runs} runs: {rewards.mean() :.2f}\n")

def train_rl(env):
    env = games.GameBase(n_decks, games.simple_rank_scores)
    agents = [A2C] #, DQN, PPO]
    for agent in agents:
        model = agent("MlpPolicy", env, verbose=1, seed=0)
        model.learn(total_timesteps=n_runs / 10, log_interval=n_runs / 100)

def main():
    env = games.GameSimulator(n_decks, games.simple_rank_scores)
    stat_methods = {
        "random"        : env.random,
        "mean score"    : env.mean_score,
        "expected score": env.expected_score, 
    }

    for name, func in stat_methods.items():
        simulate_run(env, name, func)

    env = games.GameSimulator(n_decks, games.simple_rank_scores)
    train_rl(env)
        
if __name__ == "__main__":
    main()
