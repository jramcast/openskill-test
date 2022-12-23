import game.simulation as simulation
import game.ratings as ratings
import game.ranking as ranking


print("Given the following player scores after 30 games...\n")

player_scores = simulation.play_many_times(num_players=5, num_times=30)

for player, scores in player_scores.items():
    print(" " + player, scores)



print("\n\nCalculate player ratings \n")

player_ratings = ratings.calculate_players_rating(player_scores)

for player, pratings in player_ratings.items():
    print(" " + player, pratings)


print("\n\nPlayers ranking (Convert Rating objects into ordinals and sort) \n")


players_ranking = ranking.calculate(player_ratings)

for ordinal, player in players_ranking:
    print(" " +player, ordinal)





