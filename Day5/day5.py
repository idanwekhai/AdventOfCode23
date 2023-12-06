import math
with open('input.txt') as f:
        lines = [line.strip('\n') for line in f]

seeds_1 = list(map(int, lines[0][7:].split(' ')))
seeds_2 = [range(seeds_1[a],seeds_1[a]+seeds_1[a+1]) for a in range(0, len(seeds_1)-1, 2)]
maps = lines[1:]
maps.append('')
gaps_idx = [i for i, j in enumerate(maps) if j == '']

def parse_input(maps, gaps_idx):
    maps_val = {}
    for i in range(len(maps)):
        if i in gaps_idx and gaps_idx.index(i) < len(gaps_idx)-1:
            next_gap = gaps_idx[gaps_idx.index(i) + 1] if \
            gaps_idx.index(i) < len(gaps_idx) else gaps_idx[-1]
            key = maps[i+1].strip(' map:')
            vals = [list(map(int, maps[val].split(' '))) for val in range(i+2, next_gap)]
            maps_val[key] = vals
    return maps_val

maps_val = parse_input(maps, gaps_idx)

def get_val(query, key):
    vals = maps_val[key]
    map_val_pairs = [range(v[1], v[1] + v[2]) for v in vals]
    check_key = [query in i for i in map_val_pairs]
    idx = check_key.index(True) if True in check_key else False
    if idx is not False:
        key_arr = vals[idx]
        key_idx = range(key_arr[1], key_arr[1] + key_arr[2]).index(query)
        val = range(key_arr[0], key_arr[0] + key_arr[2])[key_idx]
    else:
        val = query
    return val

min_location = math.inf
for seed in seeds_1:
    soil = get_val(seed, 'seed-to-soil')
    fertilizer = get_val(soil, 'soil-to-fertilizer')
    water = get_val(fertilizer, 'fertilizer-to-water')
    light = get_val(water, 'water-to-light')
    temperature = get_val(light, 'light-to-temperature')
    humidity = get_val(temperature, 'temperature-to-humidity')
    location = get_val(humidity, 'humidity-to-location')
    if min_location > location:
        min_location = location
print(min_location) 
