from pathlib import Path
from string import ascii_letters


with open(f"{Path(__file__).parent.absolute()}/input.txt", "r") as file:
    lines = file.readlines()


chunked_lines = [lines[i: i + 3] for i in range(0, len(lines), 3)]
priority_sum = 0

for group in chunked_lines:
    sacks = []
    for line in group:
        sacks.append(set(line))
    
    for priority, letter in enumerate(ascii_letters, 1):
        if letter in sacks[0] and letter in sacks[1] and letter in sacks[2]:
            priority_sum += priority

with open(f"{Path(__file__).parent.absolute()}/output2.txt", 'w') as file:
    file.write(str(priority_sum))
