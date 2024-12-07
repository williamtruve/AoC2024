import re
fp = open("input.txt", "r").read()
first_sec = r"^.*?don\'t\(\)"
end_sec = r"(?:do\(\)){1}(?!.*?do\(\).*?).*?$"

first = re.findall(first_sec, fp)
end = re.findall(end_sec, fp)

do_not = r'do\(\).*?don\'t\(\)'
mid_sections = re.findall(do_not, fp, re.DOTALL)
all_sections = first + mid_sections + end
def solve_section(section: str) -> int:
    regexp = r'mul\(\d+,\d+\)'
    tot = 0
    x = re.findall(regexp, section)
    new_re = r"\d+,\d+"
    for mul in x:
        digs = re.findall(new_re, mul)
        x, y = (digs[0].split(","))
        tot += int(x) * int(y)
    return tot

# Part 1
answer_1 = solve_section(fp)
print(answer_1)

# Part 2
total_sum = 0
for sec in all_sections:
    total_sum += solve_section(sec)
print(total_sum)