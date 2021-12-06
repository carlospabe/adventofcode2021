def get_initial_state(path):
    with open(path, 'r', encoding='utf-8-sig') as f:
        initial_state = list(map(int, f.read().split(',')))
        return initial_state
    

def part1(state: list):
    for day in range(80):
        new_fish = list()
        for i in range(len(state)):
            if state[i] == 0:
                new_fish.append(8)
                state[i] = 6
            else:
                state[i] -= 1
        state.extend(new_fish)
    
    return len(state)


def part2(initial_state):
    def get_state_dict(initial_state):
        state = get_defaul_state()
        for fish in initial_state:
            state[fish] += 1
        return state
    
    def get_defaul_state():
        default_state = dict()
        for i in range(9):
            default_state[i] = 0
        return default_state
    
    state = get_state_dict(initial_state)
    
    for day in range(256):
        new_state = get_defaul_state()
        new_state[8] = state[0]
        new_state[6] = state[0]
        for i in range(1, len(state)):
            new_state[i-1] += state[i]
        state = new_state.copy()
    return sum(state.values())


path = '06/06_input.txt'   
initial_state = get_initial_state(path)

print(part1(initial_state))
print(part2(initial_state))