from math import sqrt


class Chiton:
    def __init__(self, i: int, j: int, risk: int, max_len: int):
        self.id = (i, j)
        self.i = i
        self.j = j
        self.risk = risk
        self.adjs = self.get_adjs(max_len)
        self.dist = float('inf')
        self.visited = False
    
    def __repr__(self):
        return f"Ch{self.id}-{self.risk}"
    
    def get_adjs(self, max_len) -> list[tuple[int, int]]:
        adjs = [
            (self.i-1, self.j),
            (self.i, self.j-1),
            (self.i, self.j+1),
            (self.i+1, self.j)
        ]
        return [a for a in adjs if a[0] in range(max_len) and a[1] in range(max_len)]


def get_graph(file_path: str) -> dict:
    with open(file_path, 'r') as f:
        lines = f.read().splitlines()
        max_len = len(lines)
        
        chitons = dict()
        for i, line in enumerate(lines):
            for j, risk in enumerate(line):
                chitons[(i,j)] = Chiton(i, j, risk, max_len)
            
        return chitons
    
    
def dijkstra(g, origin):
    # TODO implementar dijkstra lol
    return g
    
    
def part1(chitons: dict) -> int:
    max_len = sqrt(len(chitons)) - 1
    return dijkstra(chitons, (0,0))[(max_len, max_len)].dist
    
    
file_path = '15/ex.txt'
chitons = get_graph(file_path)

print(part1(chitons))
