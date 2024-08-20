"""
Simulate and compare performance of RL agents vs statistical methods 
for a simple card game. 
"""

### Imports ###
import numpy as np
import argparse
from multiprocessing import Process, Lock
from stable_baselines3 import DQN

from cardgames import games

### CONSTANTS ###
n_decks = 1
n_runs = int(1e4 / n_decks)
total_timesteps = int(1e5)


### Low-Level Functions ###
def parse_args():
    parser = argparse.ArgumentParser(prog="Simulate Simple Card Game")
    parser.add_argument("-r", "--rl", action="store_true")

    return parser.parse_args()


def simulate_run(l, env, name, action_func):
    rewards = np.zeros((n_runs,))
    for i in range(n_runs):
        rewards[i] = sum(env.simulate_run(action_func))

    l.acquire()
    try:
        print(
            f"Using {name} method: \n"
            f"Mean reward per episode after {n_runs} runs:"
            f" {rewards.mean() :.2f}\n"
        )
    finally:
        l.release()


### High-Level Functions ###
def train_rl():
    env = games.GameBase(n_decks, games.simple_rank_scores)

    model = DQN("MlpPolicy", env, verbose=1, seed=0, exploration_final_eps=0)
    model.learn(total_timesteps=total_timesteps)


def run_stats_methods():
    env = games.GameSimulator(n_decks, games.simple_rank_scores)
    env.reset()
    stat_methods = {
        "random": env.random,
        "mean score": env.mean_observation,
        "expected score": env.expected_observation,
    }

    lock = Lock()
    for name, func in stat_methods.items():
        Process(target=simulate_run, args=(lock, env, name, func)).start()


if __name__ == "__main__":
    args = parse_args()
    if args.rl:
        train_rl()
    else:
        run_stats_methods()
