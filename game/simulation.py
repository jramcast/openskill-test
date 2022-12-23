import random

def play_many_times(num_players = 10, num_times = 30):
    """
    Generate player scores after playing "num_times"

    Scores are simulated
    """
    scores = {}

    for i in range(num_players):
        scores[f"player_{i}"] = _simulate_player_scores(num_times)

    return scores

def _simulate_player_scores(num_scores: int):
    possible_scores = list(range(1, 6))

    return [random.choice(possible_scores) for _ in range(num_scores)]
