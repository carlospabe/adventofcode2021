# only working for part 2 of the day 5 challenge

class Coord:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def __repr__(self) -> str:
        return f"[{self.x},{self.y}]"
        
    def copy(self):
        x = self.x
        y = self.y
        return Coord(x, y)


class Line:
    def __init__(self, crd1: Coord, crd2: Coord):
        self.crd1 = crd1
        self.crd2 = crd2
        
    def __repr__(self):
        return f"{self.crd1}->{self.crd2}"


def get_input(path):
    with open(path, 'r', encoding='utf-8-sig') as f:
        n = 0
        
        input_lines = f.read().splitlines()
        lines = list()
        for input_line in input_lines:
            sep = input_line.split(' ')
            crd1 = Coord(*list(map(int, sep[0].split(','))))
            crd2 = Coord(*list(map(int, sep[2].split(','))))
            
            lines.append(Line(crd1, crd2))
            n = max(n, crd1.x, crd2.x, crd1.y, crd2.y)
            
        return lines, n+1


def init_diagram(n):
    row = [0] * n
    diagram = list()
    for i in range(n):
        diagram.append(row.copy())
    return diagram


def paint_diagram(diagram, lines):
    def paint_line(line: Line, diagram):
        def update_act_crd(line:Line, act_crd: Coord):
            if line.crd1.x < line.crd2.x:
                act_crd.x += 1
            elif line.crd1.x > line.crd2.x:
                act_crd.x -= 1
            
            if line.crd1.y < line.crd2.y:
                act_crd.y += 1
            elif line.crd1.y > line.crd2.y:
                act_crd.y -= 1
            
            return act_crd
        
        def in_bounds(line: Line, act_crd: Coord):
            min_x = min(line.crd1.x, line.crd2.x)
            max_x = max(line.crd1.x, line.crd2.x)
            min_y = min(line.crd1.y, line.crd2.y)
            max_y = max(line.crd1.y, line.crd2.y)
            
            in_bounds_x = min_x <= act_crd.x <= max_x
            in_bounds_y = min_y <= act_crd.y <= max_y
            return in_bounds_x and in_bounds_y
        
        act_crd = line.crd1.copy()
        while in_bounds(line, act_crd):
            diagram[act_crd.y][act_crd.x] += 1
            act_crd = update_act_crd(line, act_crd)
        return diagram
        
    for line in lines:
        diagram = paint_line(line, diagram)
        
    return diagram


def get_overlaps(diagram):
    overlaps = 0
    for row in diagram:
        for i in row:
            if i >= 2: overlaps += 1
    return overlaps


path = '05/05_input.txt'         
lines, n = get_input(path)
diagram = init_diagram(n)
diagram = paint_diagram(diagram, lines)
for i in diagram:
    print(i)
overlaps = get_overlaps(diagram)
print(overlaps)
