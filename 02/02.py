def get_instructions():
    with open("02/02_input.txt", 'r', encoding='utf-8-sig') as f:
        lines = f.read().splitlines()
    
    instructions = list()
    for line in lines:
        command, units = line.split()
        instruction = dict()
        instruction['command'] = str(command)
        instruction['units'] = int(units)
        instructions.append(instruction)
    
    return instructions


def part_1(instructions):
    position = {
        'horizontal': 0,
        'depth': 0
    }
    for inst in instructions:
        if inst['command'] == "forward":
            position['horizontal'] += inst['units']
        elif inst['command'] == "up":
            position['depth'] -= inst['units']
        else:  # inst['command'] == "down"
            position['depth'] += inst['units']
            
    return position['depth'] * position['horizontal']


def part_2(instructions):
    position = {
        'horizontal': 0,
        'depth': 0,
        'aim': 0
    }
    for inst in instructions:
        if inst['command'] == "forward":
            position['horizontal'] += inst['units']
            position['depth'] += position['aim'] * inst['units']
        elif inst['command'] == "up":
            position['aim'] -= inst['units']
        else:  # inst['command'] == "down"
            position['aim'] += inst['units']
            
    return position['depth'] * position['horizontal']


instructions = get_instructions()

print(part_1(instructions))
print(part_2(instructions))