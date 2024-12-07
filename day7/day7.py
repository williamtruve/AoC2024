fp = open("input.txt", "r").readlines()
from tqdm import tqdm
wins = 0
for line in tqdm(fp):
    total, numbers = line.split(":")
    numbers = numbers.split()
    attempts = [int(numbers[0])]
    for num in numbers[1:]:
        new_attempts = []
        for att in attempts:
            new_sum = att+int(num)
            new_prod = att*int(num)
            new_append = int(str(att)+num)

            new_attempts.append(new_sum)
            new_attempts.append(new_prod)
            new_attempts.append(new_append)
        attempts = new_attempts
    if int(total) in attempts:
        wins += int(total)
print(wins)