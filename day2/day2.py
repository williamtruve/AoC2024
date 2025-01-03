from more_itertools import difference, is_sorted

fp = open("input.txt").readlines()
totsum = 0


def evaluate_line(line, problem_damp=False):
    diffs = list(difference(line, initial=0))
    diff_too_big = list(map(lambda x: abs(x) > 3, diffs))
    if (
        is_sorted(line, strict=True) or is_sorted(line, reverse=True, strict=True)
    ) and not any(diff_too_big):
        return 1
    elif problem_damp:
        for ix in range(len(line)):
            if evaluate_line(line[0:ix] + line[ix + 1 :]) == 1:
                return 1
    return 0


for line in fp:
    parsed_line = list(map(int, line.split()))
    totsum += evaluate_line(parsed_line, False)
print(totsum)
