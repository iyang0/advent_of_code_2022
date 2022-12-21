from pathlib import Path

with open(f"{Path(__file__).parent.absolute()}/input.txt", "r") as file:
    lines = file.readlines()

score = 0
for line in lines:
    opponent, me = line.split()
    score += {
        'X': 1,
        'Y': 2,
        'Z': 3
    }[me]
    score += {
        ('A', 'X'): 3,
        ('A', 'Y'): 6,
        ('A', 'Z'): 0,
        ('B', 'X'): 0,
        ('B', 'Y'): 3,
        ('B', 'Z'): 6,
        ('C', 'X'): 6,
        ('C', 'Y'): 0,
        ('C', 'Z'): 3,
    }[(opponent, me)]

with open(f"{Path(__file__).parent.absolute()}/output.txt", 'w') as file:
    file.write(str(score)+"\n")