# passed both part 1 and 2 of the day 1 challenge

import sys


with open('01/01_input.txt', 'r', encoding='utf-8-sig') as f:
    msments = list(map(int, f.read().splitlines()))


def part_1(msments):
    prev_msment = sys.maxsize
    n_incr = 0
    for msment in msments:
        if msment > prev_msment:
            n_incr += 1
        prev_msment = msment

    return n_incr


def part_2(msments):
    prev_sum_3 = sys.maxsize
    n_incr = 0
    for i in range(len(msments)-2):
        sum_3 = msments[i] + msments[i+1] + msments[i+2]

        if sum_3 > prev_sum_3:
            n_incr += 1
        prev_sum_3 = sum_3
    
    return n_incr


print(part_1(msments))
print(part_2(msments))
