from collections import Counter

fp = open("input.txt").readlines()
xs = []
ys = []
for line in fp:
    x, y = line.split()
    xs.append(int(x))
    ys.append(int(y))
xs.sort()
ys.sort()
tot_sum = 0

# Part 1
for x,y in zip(xs, ys):
    tot_sum += abs(x-y)
print(tot_sum)

# Part 2
tot_sum = 0
y_counter = Counter(ys)
for x in xs:
    tot_sum += x*y_counter[x]
print(tot_sum)