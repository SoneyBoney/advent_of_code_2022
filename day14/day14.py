from typing import Optional, Set, Tuple


def parse_pair(pair_str: str) -> Tuple[int, int]:
    temp = pair_str.split(",")
    return (int(temp[0]), int(temp[1]))


def parse_rocks(line: str) -> Set[Tuple[int, int]]:
    ret = set()
    pairs = [pair.strip() for pair in line.split("->")]

    for i in range(len(pairs) - 1):
        last_pair = parse_pair(pairs[i])
        next_pair = parse_pair(pairs[i + 1])
        x_min, x_max = min(last_pair[0], next_pair[0]), max(last_pair[0], next_pair[0])
        y_min, y_max = min(last_pair[1], next_pair[1]), max(last_pair[1], next_pair[1])
        # print((x_min,y_min),(x_max,y_max))
        for x_index in range(x_min, x_max + 1):
            for y_index in range(y_min, y_max + 1):
                ret.add((x_index, y_index))
    # print(ret)
    return ret


def find_next_spot(
    current_spot: Tuple[int, int], grid: Set[Tuple[int, int]]
) -> Optional[Tuple[int, int]]:
    down_step = (current_spot[0],current_spot[1]+1)
    diag_left = (current_spot[0]-1,current_spot[1]+1)
    diag_right = (current_spot[0]+1,current_spot[1]+1)
    if down_step not in grid:
        return down_step
    elif diag_left not in grid:
        return diag_left
    elif diag_right not in grid:
        return diag_right
    else:
        return None

# def drop_sand(current: Tuple[int,int], grid: Set[Tuple[int, int]]) -> bool:
#     bottom = max(grid,key=lambda x: x[1])
#     last_spot = current
#     while (next_spot := find_next_spot(last_spot,grid)) is not None:
#         if next_spot[1] > bottom[1]:
#             return True
#         print(next_spot)
#         last_spot = next_spot
#     grid.add(last_spot)
#     return False

# with open("test.txt", "r") as f:
#     data = f.read().split("\n")[:-1]

#     grid = set()

#     for line in data:
#         grid = grid.union(parse_rocks(line))
#     sand_origin = (500, 0)
#     sand_counter = 0
#     while True:
#         is_abyss = drop_sand(sand_origin, grid)
#         if is_abyss:
#             break
#         sand_counter += 1
#     print(sand_counter)
# pt 2
def drop_sand_pt2(current: Tuple[int,int], grid: Set[Tuple[int, int]], depth: int) -> Optional[bool]:
    last_spot = current
    while (next_spot := find_next_spot(last_spot,grid)) is not None:
        if next_spot[1] >= depth:
            #print('break', last_spot)
            grid.add(last_spot)
            return False
        last_spot = next_spot
        #print(depth, next_spot, depth)
    grid.add(last_spot)
    if last_spot == current:
        return True
    return False

with open("input.txt", "r") as f:
    data = f.read().split("\n")[:-1]

    grid = set()

    for line in data:
        grid = grid.union(parse_rocks(line))
    depth = max(grid,key=lambda x: x[1])[1] + 2
    sand_origin = (500, 0)
    sand_counter = 0
    while True:
        ret = drop_sand_pt2(sand_origin, grid, depth)
        if ret:
            break
        sand_counter += 1
    print(sand_counter+1)

