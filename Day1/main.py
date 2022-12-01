

SAMPLE_DATA: bool = False
if SAMPLE_DATA:
    filename = "sample_data.txt"
else:
    filename = "data.txt"

with open(filename, 'r') as f:
    lines = [line.strip() for line in f.readlines()]

calories = []

curr_cal = 0
for line in lines:
    if len(line) == 0:
        calories.append(curr_cal)
        curr_cal = 0
    else:
        curr_cal += int(line)
calories = sorted(calories, reverse=True)
print(f'Part 1: {calories[0]}')
sum_top_three = sum(sorted(calories, reverse=True)[:3])
print(f'Part 2: {sum_top_three}')