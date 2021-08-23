"""
TOURNAMENT WINNER EXAMPLE SOLUTION
"""

HOME_TEAM_WON = 1


def tournament_winner(competitions, results):
    best_team = ""
    scores = {best_team: 0}

    for idx, competition in enumerate(competitions):
        result = results[idx]
        home_team, away_team = competition

        winner = home_team if result == HOME_TEAM_WON else away_team

        update_scores(winner, 3, scores)

        if scores[winner] > scores[best_team]:
            best_team = winner

    return best_team


def update_scores(team, points, scores):
    if team not in scores:
        scores[team] = 0

    scores[team] += points


#######################################################

# Test cases -- winner is 'Dolphins'

# competitions = [
#     ['Panthers', 'Lionesses'],
#     ['Lionesses', 'Dolphins'],
#     ['Dolphins', 'Panthers'],
# ]
#
# results = [0, 0, 1]

#######################################################

# Test cases -- winner is 'D'

# competitions = [
#     ['A', 'B'],
#     ['B', 'C'],
#     ['C', 'A'],
#     ['D', 'C'],
#     ['E', 'D'],
#     ['D', 'A'],
# ]
#
# results = [0, 1, 1, 1, 0, 1]

#######################################################

# Test cases -- winner is 'Lionesses'

competitions = [
    ['Panthers', 'Lionesses'],
    ['Panthers', 'Dolphins'],
    ['Dolphins', 'Lionesses'],
]

results = [0, 0, 0]

#######################################################

print(tournament_winner(competitions, results))
