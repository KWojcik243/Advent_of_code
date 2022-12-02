file = open("2022\day_2\input_day_2.txt", 'r')

#First part

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

score = 0

for line in file:
    score+=results[line.strip()]

print(score)

#Second part

