from pathlib import Path
from typing import List

with open(f"{Path(__file__).parent.absolute()}/input.txt", "r") as file:
    lines = file.readlines()

most: List[int] = []
current: int = 0

for line in lines:
    if line == "\n":
        most.append(current)
        current = 0
        continue
    else:
        num = int(line.strip())
        current += num

most = sorted(most, reverse=True)[:3]

with open(f"{Path(__file__).parent.absolute()}/output.txt", 'w') as file:
    file.write(str(most[0])+"\n")
    file.write(str(most[0]+most[1]+most[2]))
