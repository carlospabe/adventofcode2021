from os import X_OK


def get_cavemap(file_path) -> dict:
    def add_adj(key, adj):
        if key in cavemap:
            cavemap[key].append(adj)
        else:
            cavemap[key] = [adj]
            
    with open(file_path, 'r') as f:
        cavemap = dict()
        lines = f.read().splitlines()
        for line in lines:
            c1, c2 = line.split('-')
            
            if 'start' in line:
                if c1 == 'start':
                    add_adj('start', c2)
                else:
                    add_adj('start', c1)
            elif 'end' in line:
                if c1 == 'end':
                    add_adj(c2, 'end')
                else:
                    add_adj(c1, 'end')
                    
            else:
                add_adj(c1, c2)
                add_adj(c2, c1)
        
        cavemap['end'] = list()
        return cavemap


def get_paths(paths, cave: str, cavemap, path: list):
    if cave == 'end':
        # print(*path, sep=',')
        return paths + 1
    else:
        for adj in cavemap[cave]:
            if adj not in path or not adj.islower():
                
                path.append(adj)
                paths = get_paths(paths, adj, cavemap, path)
                path.pop()
    return paths


def get_paths_2(paths, cave: str, cavemap, path: list):
    def is_suitable(c, path):
        def is_any_lower_repeated(path):
            def ocurrences(c, path):
                return len([x for x in path if x == c])
            
            repeated = False
            lower_in_path = [x for x in path if x.islower()]
            for i in lower_in_path:
                if ocurrences(i, path) > 1:
                    repeated = True
                    break
            return repeated
        if not c.islower():
            is_suitable = True
        else:
            is_suitable = not (is_any_lower_repeated(path) and c in path)
        return is_suitable

    if cave == 'end':
        # print(*path, sep=',')
        return paths + 1
    else:
        for adj in cavemap[cave]:
            if is_suitable(adj, path):
                path.append(adj)
                paths = get_paths_2(paths, adj, cavemap, path)
                path.pop()
    return paths


def part1(cavemap: dict) -> int:
    path = ['start']
    paths = 0
    paths = get_paths(paths, 'start', cavemap, path)
    return paths


def part2(cavemap: dict) -> int:
    path = ['start']
    paths = 0
    paths = get_paths_2(paths, 'start', cavemap, path)
    return paths


file_path = '12/12_input.txt'
cavemap = get_cavemap(file_path)
print(part1(cavemap))
print(part2(cavemap))
            