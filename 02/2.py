
POINT_MAP = {'A':1, 'B':2, 'C':3}
OUTCOME_POINT_MAP = {'X': 0, 'Y': 3, 'Z': 6}
# A, X Rock
# B, Y Paper
# C, Z Scissors
# There are 9 combinations, 3 winning, 3 losing, 3 draws. We can map only winning (6) and lose (0) and use Draw (3) as def

#
WINNING_MAP = {'A':'B', 'B':'C', 'C':'A'}
LOSING_MAP = {'A':'C', 'B':'A', 'C':'B'}

with open("input_test") as file:
    lines = file.readlines()

score = 0

for line in lines:
    line = line.strip()
    played, required_outcome = line.split(' ')
    score += OUTCOME_POINT_MAP[required_outcome]
    if required_outcome == 'X':
        #Lose
        score += POINT_MAP[LOSING_MAP[played]]
    elif required_outcome == 'Z':
        #Win
        score += POINT_MAP[WINNING_MAP[played]]
    else:
        #Tie
        score += POINT_MAP[played]


print(score)