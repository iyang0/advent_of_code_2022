from pathlib import Path

with open(f"{Path(__file__).parent.absolute()}/input.txt", "r") as file:
    lines = file.readlines()

score = 0
for line in lines:
    opponent, me = line.split()
    score += {
        'X': 0,
        'Y': 3,
        'Z': 6
    }[me]
    score += {
        ('A', 'X'): 3,
        ('A', 'Y'): 1,
        ('A', 'Z'): 2,
        ('B', 'X'): 1,
        ('B', 'Y'): 2,
        ('B', 'Z'): 3,
        ('C', 'X'): 2,
        ('C', 'Y'): 3,
        ('C', 'Z'): 1,
    }[(opponent, me)]

with open(f"{Path(__file__).parent.absolute()}/output2.txt", 'w') as file:
    file.write(str(score)+"\n")