def get_lines(path):
    with open(path, 'r', encoding='utf-8-sig') as f:
        return f.read().splitlines()
    

def part1(lines):
    def get_error_score(illegal_chars):
        score = {
            ')': 3,
            ']': 57,
            '}': 1197,
            '>': 25137,
            }
        return sum([sc for sc in [score[c] for c in illegal_chars]])
    
    openers = ['(', '[', '{', '<']
    key = {
        '(': 1,
        ')': 1,
        '[': 2,
        ']': 2,
        '{': 3,
        '}': 3,
        '<': 4,
        '>': 4,
    }
    illegal_chars = list()
    for line in lines:
        openers_encountered = list()
        for char in line:
            if char in openers:
                openers_encountered.append(char)
            elif key[openers_encountered[-1]] == key[char]:
                openers_encountered.pop()
            else:
                illegal_chars.append(char)
                break
                
    return get_error_score(illegal_chars)


def part2(lines: list):
    def get_score(openers: list):
        points = {
            '(': 1,
            '[': 2,
            '{': 3,
            '<': 4,
        }
        score = 0
        openers.reverse()
        for o in openers:
            score *= 5
            score += points[o]
        return score
            
            
    openers = ['(', '[', '{', '<']
    key = {
        '(': 1,
        ')': 1,
        '[': 2,
        ']': 2,
        '{': 3,
        '}': 3,
        '<': 4,
        '>': 4,
    }
    corrupted = False
    scores = list()
    for line in lines.copy():
        openers_encountered = list()
        for char in line:
            if char in openers:
                openers_encountered.append(char)
            elif key[openers_encountered[-1]] == key[char]:
                openers_encountered.pop()
            else:
                corrupted = True
                break
        if not corrupted:
            scores.append(get_score(openers_encountered))
        else:
            corrupted = False
    
    return sorted(scores)[(len(scores)-1)//2]


path = '10/10_input.txt'
lines = get_lines(path)

print(part1(lines))
print(part2(lines))
