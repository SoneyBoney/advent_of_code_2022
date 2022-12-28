def parse_three_tuple(line: str):
    one, two, three = line.split(",")
    return (int(one), int(two), int(three))


def new_threeple(threeple, index, new):
    if index == 0:
        return (new, threeple[1], threeple[2])
    elif index == 1:
        return (threeple[0], new, threeple[2])
    elif index == 2:
        return (threeple[0], threeple[1], new)


def get_surface_area(drop, blobs):
    neighbors = set()
    for index in range(3):
        for i in [-1, 1]:
            neighbors.add(new_threeple(drop, index, drop[index] + i))
    surface_area = 6 - len(blobs.intersection(neighbors))
    return surface_area


# with open("input.txt", "r") as f:
#     data = f.read().split("\n")[:-1]

#     blobs = set()

#     for line in data:
#         blobs.add(parse_three_tuple(line))
#     ret = 0
#     for b in blobs:
#         ret += get_surface_area(b,blobs)

#     print(ret)
# pt 2
from typing import Set, Tuple


def get_neighbors(point: Tuple[int, int, int]):
    x, y, z = point
    return [
        (x - 1, y, z),
        (x + 1, y, z),
        (x, y - 1, z),
        (x, y + 1, z),
        (x, y, z - 1),
        (x, y, z + 1),
    ]


# do a BFS kind of thing to see if a point is in the interior of the blobs
# If it is, all the blobs should form a perimeter/boundary
def trapped(
    point: Tuple[int, int, int],
    all_blobs: Set[Tuple[int, int, int]],
    interior: Set[Tuple[int, int, int]],
    exterior: Set[Tuple[int, int, int]],
    limit: int = 10000,
):
    # check memoized
    if point in interior:
        return True
    if point in exterior:
        return False
    visited = set()
    queue = [point]
    i = 0
    while queue:
        i += 1
        current_point = queue.pop(0)

        if current_point in all_blobs:
            continue
        if current_point in visited:
            continue
        visited.add(current_point)
        queue += get_neighbors(current_point)
        if i > limit:
            # Limit reached, assume it is not in interior
            # add visited points since they are path connected to the exterior
            for point in visited:
                exterior.add(point)
            return False
    # add visited points since none of them are on the outside
    for point in visited:
        interior.add(point)
    return True  # if point is trapped, then the loop will terminate


with open("input.txt", "r") as f:
    data = f.read().split("\n")[:-1]

    blobs = set()
    interior = set()
    exterior = set()
    for line in data:
        blobs.add(parse_three_tuple(line))
    ret = 0
    for b in blobs:
        for point in get_neighbors(b):
            if not trapped(point, blobs, interior, exterior):
                ret += 1

    print(ret)
