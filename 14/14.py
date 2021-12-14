from collections import Counter


def get_input(file_path):
    with open(file_path, 'r') as f:
        lines = f.read().splitlines()
        template = list(lines[0])            
        pairs = {p:i for p, a, i in [line.split(' ') for line in lines[2:]]}
    return template, pairs


def part1(polym: list, pairs: dict, steps: int) -> int:
    for step in range(steps):
        n_ins = 0
        polym_cp = polym.copy()
        for i in range(len(polym)-1):
            pair = polym_cp[i] + polym_cp[i+1]
            polym.insert(i+1+n_ins, pairs[pair])
            n_ins +=1
        print(f"step {step+1} done")
    
    ocurs = dict()
    for e in polym:
        if e in ocurs:
            ocurs[e] += 1
        else:
            ocurs[e] = 1
    
    return max(ocurs.values()) - min(ocurs.values())


def count_for_cicle(polymer, patterns, cicle):
    elements = Counter(polymer)
    parts = Counter([polymer[i] + polymer[i + 1] for i in range(len(polymer) - 1)])

    for _ in range(cicle):
        parts, old_parts = Counter(), parts

        for (a, b), add in patterns.items():
            parts[a + add] += old_parts[a + b]
            parts[add + b] += old_parts[a + b]
            elements[add] += old_parts[a + b]
    return elements


file_path = '14/14_input.txt'
template, pairs = get_input(file_path)

print(part1(template, pairs, 10))
elements = count_for_cicle(template, pairs, 40)
print(max(elements.values()) - min(elements.values()))