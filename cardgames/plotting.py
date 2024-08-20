### Imports ###
import numpy as np
import collections

import plotly.graph_objects as go

from cardgames.games import GameSimulator
from cardgames.games import simple_rank_scores
from cardgames.utils import ranks, Card, Hand, Deck


### Plotting Functions ###
def plot_distribution(game: GameSimulator):
    x = list(ranks.keys())
    observations = np.sort(game.observation_distribution())
    counter = collections.Counter(observations)
    y = list(counter.values())

    fig = go.Figure()
    fig.add_trace(go.Bar(x=x, y=y, name="Number of Cards", marker_color="red"))

    fig.update_layout(
        title_text="Distribution of Remaining Cards",
        xaxis_title="Rank",
        yaxis_title="Number of Cards Remaining",
        font=dict(
            size=20,
            family="arial",
            weight="bold",
        ),
    )

    return fig


if __name__ == "__main__":
    game = GameSimulator(1, simple_rank_scores)
    game.reset()

    fig = plot_distribution(game)
    fig.show()
