from typing import Dict, List, Tuple
from openskill import ordinal, Rating

def calculate(player_ratings: Dict[str, Rating]) -> List[Tuple[float, str]]:
    """
    Calculate a players ranking based on player Rating objects
    """

    # Convert a rating obj (mu and sigma) into a single ordinal value
    # to be able to sort
    ordinals = { p: ordinal(rating) for p, rating in player_ratings.items() }

    ranking = []

    for player, player_ordinal in ordinals.items():
        ranking.append((player_ordinal, player))

    ranking = sorted(ranking, reverse=True)

    return ranking
