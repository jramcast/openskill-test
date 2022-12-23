import statistics
from openskill import Rating
from typing import Dict, List


def calculate_players_rating(players_scores: Dict[str, List[int]]):
    ratings = {}

    for player, scores in players_scores.items():
        ratings[player] = calculate_single_player_stats(scores)

    return ratings

def calculate_single_player_stats(scores: List[int]):
    mean = statistics.mean(scores)
    standard_dev = statistics.stdev(scores)
    return Rating(mu=mean, sigma=standard_dev)
