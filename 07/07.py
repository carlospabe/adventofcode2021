import sys


def get_input(path):
    with open(path, 'r', encoding='utf-8-sig') as f:
        input = list(map(int, f.read().split(',')))
        return input


def part1(input):
    min_fuel = sys.maxsize
    for pos_dest in range(len(input)):
        wasted_fuel = 0
        for i in range(len(input)):
            wasted_fuel += abs(input[i] - pos_dest)
        min_fuel = min(min_fuel, wasted_fuel)
    return min_fuel


def part2(input):
    def get_wasted_fuel(a, b):
        wasted_fuel = 0
        if not a == b:
            for i in range(abs(a-b)):
                wasted_fuel += i+1                
        return wasted_fuel
        
    min_fuel = sys.maxsize
    for pos_dest in range(len(input)):
        wasted_fuel = 0
        for i in range(len(input)):
            wasted_fuel += get_wasted_fuel(input[i], pos_dest)
        min_fuel = min(min_fuel, wasted_fuel)
    return min_fuel


path = '07/07_input.txt'
input = get_input(path)
print(part1(input))
print(part2(input))
