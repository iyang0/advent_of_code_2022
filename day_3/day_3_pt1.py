from pathlib import Path
from string import ascii_letters


with open(f"{Path(__file__).parent.absolute()}/input.txt", "r") as file:
    lines = file.readlines()

priority_sum = 0
for line in lines:
    half_len = len(line)//2
    left, right = set(line[:half_len]), set(line[half_len:])
    
    intersection = left.intersection(right).pop()
    # print(ord(intersection.pop()))
    for priority, letter in enumerate(ascii_letters, 1):
        if intersection == letter:
            priority_sum += priority

with open(f"{Path(__file__).parent.absolute()}/output.txt", 'w') as file:
    file.write(str(priority_sum))
