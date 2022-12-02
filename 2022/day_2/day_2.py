file = open("2022\day_2\input_day_2.txt", 'r')

results = {
    "A X":4,
    "A Y":8,
    "A Z":3,
    "B X":1,
    "B Y":5,
    "B Z":9,
    "C X":7,
    "C Y":2,
    "C Z":6,
}

results_with_strategy = {
    "A X":3,
    "A Y":4,
    "A Z":8,
    "B X":1,
    "B Y":5,
    "B Z":9,
    "C X":2,
    "C Y":6,
    "C Z":7,
}

score = 0
score_with_strategy = 0

for line in file:
    line = line.strip()
    score+=results[line]
    score_with_strategy+=results_with_strategy[line]

print(score)
print(score_with_strategy)
