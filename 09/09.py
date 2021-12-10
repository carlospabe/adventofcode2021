class Location:
    def __init__(self, height, i, j, adjs=list()):
        self.id = f"{i}-{j}"
        self.height = height
        self.i = i
        self.j = j
        self.adjs = adjs
        
    def __repr__(self):
        return f"ID:{self.id} - H:{self.height} - {self.adjs}"


def get_heightmap(path):
    with open(path, 'r', encoding='utf-8-sig') as f:
        heightmap = list()
        lines = f.read().splitlines()
        for line in lines:
            row = [int(digit) for digit in line]
            heightmap.append(row)
            
        return heightmap


def get_locations(heightmap):
    def get_adjs(heightmap, i, j):
        adjs = list()
        rows = len(heightmap)
        cols = len(heightmap[0])
        
        if i > 0:
            adjs.append(f"{i-1}-{j}")
        if i < rows-1:
            adjs.append(f"{i+1}-{j}")
        if j > 0:
            adjs.append(f"{i}-{j-1}")
        if j < cols-1:
            adjs.append(f"{i}-{j+1}")
        
        return adjs
    
    def initialize_locations(heightmap, rows, cols):
        locations = dict()
        for i in range(rows):
            for j in range(cols):
                loc_height = heightmap[i][j]
                new_location = Location(loc_height, i, j)
                locations[new_location.id] = new_location
        return locations
    
    def set_adjs(heightmap, locations, rows, cols):
        for i in range(rows):
            for j in range(cols):
                loc_id = f"{i}-{j}"
                locations[loc_id].adjs = get_adjs(heightmap, i, j)
        return locations
    
    rows = len(heightmap)
    cols = len(heightmap[0])
    locations = initialize_locations(heightmap, rows, cols)
    locations = set_adjs(heightmap, locations, rows, cols)
    return locations


def get_low_points(locations: dict):
    low_points = list()
    for loc in locations.values():
        if all(locations[adj].height > loc.height for adj in loc.adjs):
            low_points.append(loc.id)
    return low_points


def part1(heightmap: list(list())): 
    locations = get_locations(heightmap)
    low_points = get_low_points(locations)
    
    risk_levels = [locations[loc_id].height + 1 for loc_id in low_points]
    total_risk = sum(risk_levels) 
    return total_risk


def part2(heightmap):
    def get_all_basins(locations, low_points):
        def get_basin(locations, low_pt, basin):
            for adj in locations[low_pt].adjs:
                if locations[adj].height < 9 and adj not in basin:
                    basin.append(adj)
                    get_basin(locations, adj, basin)
            return basin
        
        basins = list()
        for low_pt in low_points:
            basin = [low_pt]
            basin = get_basin(locations, low_pt, basin)
            basins.append(basin)
        return basins
    
    locations = get_locations(heightmap)
    low_points = get_low_points(locations)
    
    basins = get_all_basins(locations, low_points)
    
    basins = sorted(basins, key=len, reverse=True)[:3]
    sizes_mult = 1
    for b in basins:
        sizes_mult *= len(b)
    return sizes_mult


path = '09/09_input.txt'
heightmap = get_heightmap(path)

print(part1(heightmap))
print(part2(heightmap))