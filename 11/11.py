class Octopus:
    def __init__(self, e_lvl: int, i: int, j: int):
        self.id = (i, j)
        self.e_lvl = e_lvl
        self.i = i
        self.j = j
        self.adjs = self.set_adjs()
        
    def __repr__(self):
        return f"{self.id} - {self.e_lvl}"
    
    def inc_e(self, inc: int):
        self.e_lvl += inc
        
    def set_adjs(self):
        adjs = [
            (self.i-1, self.j-1),
            (self.i-1, self.j),
            (self.i-1, self.j+1),
            (self.i, self.j-1),
            (self.i, self.j+1),
            (self.i+1, self.j-1),
            (self.i+1, self.j),
            (self.i+1, self.j+1)
        ]
        for adj in adjs.copy():
            i, j = adj
            if i < 0 or j < 0 or i > 9 or j > 9:
                adjs.remove(adj)
        return adjs


def get_grid(path: str) -> dict[Octopus]:
    with open(path, 'r', encoding='utf-8-sig') as f:
        grid = dict()
        input = f.read().splitlines()
        for i in range(10):
            for j in range(10):
                new_octopus = Octopus(int(input[i][j]), i, j)
                grid[new_octopus.id] = new_octopus

        return grid


def flash(octopus: Octopus, flashes: int, grid: dict[tuple[int, int], Octopus]):
    octopus.e_lvl = 0
    for adj_id in octopus.adjs:
        if grid[adj_id].e_lvl != 0:
            grid[adj_id].inc_e(1)
    for adj_id in octopus.adjs:
        if grid[adj_id].e_lvl > 9:
            flashes, grid = flash(grid[adj_id], flashes, grid)
    return flashes+1, grid


def inc_e_lvl(grid: dict[Octopus]) -> dict[Octopus]:
        for octopus in grid.values():
            octopus.inc_e(1)
        return grid

def part1(grid: dict[Octopus]) -> int:
    flashes = 0
    steps = 100
    for step in range(steps):
        grid = inc_e_lvl(grid)
        for octopus in grid.values():
            if octopus.e_lvl > 9:
                flashes, grid = flash(octopus, flashes, grid)
    return flashes


def part2(grid: dict[tuple[int, Octopus]]) -> int:
    flashes = 0
    step = 1
    while 1:
        grid = inc_e_lvl(grid)
        for octopus in grid.values():
            if octopus.e_lvl > 9:
                flashes, grid = flash(octopus, flashes, grid)
        if all(octopus.e_lvl == 0 for octopus in grid.values()):
            return step
        step += 1
        

path = '11/11_input.txt'
grid = get_grid(path)

print(part1(grid))
print(part2(grid))
