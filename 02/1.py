
POINT_MAP = {'X':1, 'Y':2, 'Z':3}
# A, X Rock
# B, Y Paper
# C, Z Scissors
# There are 9 combinations, 3 winning, 3 losing, 3 draws. We can map only winning (6) and lose (0) and use Draw (3) as def
OUTCOME_MAP = {'A Y': 6, 'A Z':0, 'B X': 0, 'B Z': 6, 'C X': 6, 'C Y': 0}

with open("input_1") as file:
    lines = file.readlines()

score = 0

for line in lines:
    line = line.strip()
    print(OUTCOME_MAP.get(line, 3), POINT_MAP[line.split(' ')[1]])
    score += OUTCOME_MAP.get(line, 3) + POINT_MAP[line.split(' ')[1]]
    print(score)

print(score)