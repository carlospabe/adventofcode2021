class Dot:
    def __init__(self, x, y):
        self.i = int(y)
        self.j = int(x)
    
    def __repr__(self):
        return f"Dot[{self.i},{self.j}]"
    
    def set_i(self, i):
        self.i = i
        
    def set_j(self, j):
        self.j = j
        
    def __eq__(self, other: object) -> bool:
        if isinstance(other, Dot):
            return self.i == other.i and self.j == other.j
        return False
    
    
class FoldInst:
    def __init__(self, axis, value):
        self.axis = str(axis)
        self.value = int(value)
    
    def __repr__(self):
        return f"FoldInst({self.axis}={self.value})"


def get_input(file_path):
    with open(file_path, 'r') as f:
        lines = f.read().splitlines()
        
        dot_lines = [line for line in lines if ',' in line]
        dots = [Dot(*dot_line.split(',')) for dot_line in dot_lines]
        
        fold_lines = [line for line in lines if 'fold' in line]
        fold_pars = [fold_line.split(' ')[-1] for fold_line in fold_lines]
        fold_insts = [FoldInst(*fold_par.split('=')) for fold_par in fold_pars]
        
        return dots, fold_insts
    

def fold(dots: list[Dot], fold_inst: FoldInst) -> list[Dot]:
    # y afecta a i (y=1 recta horizontal en 1)
    # x afecta a j (x=1 recta vertical en 1)
    
    def fold_x(dots: list[Dot], fold_inst: FoldInst) -> list[Dot]:
        new_dots = [dot for dot in dots if dot.j < fold_inst.value]
        changing_dots = [dot for dot in dots if dot not in new_dots]
        for new_dot in changing_dots:
            new_j = fold_inst.value - (new_dot.j - fold_inst.value)
            new_dot.set_j(new_j)
            if new_dot not in new_dots:
                new_dots.append(new_dot)
        return new_dots
    
    def fold_y(dots: list[Dot], fold_inst: FoldInst) -> list[Dot]:
        new_dots = [dot for dot in dots if dot.i < fold_inst.value]
        changing_dots = [dot for dot in dots if dot not in new_dots]
        for new_dot in changing_dots:
            new_i = fold_inst.value - (new_dot.i - fold_inst.value)
            new_dot.set_i(new_i)
            if new_dot not in new_dots:
                new_dots.append(new_dot)
        return new_dots
    
    if fold_inst.axis == 'x':
        dots = fold_x(dots, fold_inst)
    else:  #fold_inst.axis == 'y'
        dots = fold_y(dots, fold_inst)
    return dots


def part1(dots: list[Dot], fold_insts: list[FoldInst]) -> int:
    fold_inst = fold_insts[0]
    dots = fold(dots, fold_inst)
    return len(dots)


def part2(dots: list[Dot], fold_insts: list[FoldInst]) -> str:
    def get_2d_str(dots: list[Dot]) -> str:
        max_x = max([dot.j for dot in dots])
        max_y = max([dot.i for dot in dots])
        
        line = ['.'] * (max_x + 1)
        lines = [line.copy() for y in range(max_y + 1)]
            
        string = str()
        for dot in dots:
            lines[dot.i][dot.j] = '#'
        
        for line in lines:
            for c in line:
                string += c
            string += '\n'
        return string
        
    for fold_inst in fold_insts:
        dots = fold(dots, fold_inst)
        
    return get_2d_str(dots)

    
file_path = '13/13_input.txt'
dots, fold_insts = get_input(file_path)

print(part1(dots, fold_insts))
print(part2(dots, fold_insts))
       