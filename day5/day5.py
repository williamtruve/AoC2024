from functools import cmp_to_key
fp = open("input.txt", "r").read()

ordering, updates = fp.split("\n\n")
ordering = ordering.split("\n")
updates = updates.split("\n")

from collections import defaultdict

order_dict = defaultdict(list)
for ordering_rule in ordering:
    x, y = ordering_rule.split("|")
    order_dict[x].append(y)
def cmpValue(x, y):
    return int(y in order_dict[x])
def make_comparator(less_than):
    def compare(x, y):
        if less_than(x, y):
            return -1
        elif less_than(y, x):
            return 1
        else:
            return 0
    return compare
your_key = cmp_to_key(make_comparator(cmpValue))
p1_score = 0
p2_score = 0
for update in updates:
    bad_update = False
    seen_numbers = []
    update = update.split(",")
    for number in update:
        seen_numbers.append(number)
        for forbidden in order_dict[number]:
            if forbidden in seen_numbers:
                bad_update = True
    if bad_update:
        update = sorted(update, key=your_key)
        p2_score += int(update[int(len(update)/2)])
    else:
        p1_score += int(update[int(len(update)/2)])
print(p1_score, p2_score)
