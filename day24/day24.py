from typing import List, Set, Tuple

# graph states are cyclic
# compute all states
# run djikstras or smthing

# total states == board size 
def create_graph_masks(board: List[str]) -> List[Set[Tuple[int,int]]]:
    ret = []
    width = len(board[0]) - 2 
    height = len(board) - 2
    for time in range(width*height +1):
        temp_mask = set()
        for y,line in enumerate(board):
            for x,elem in enumerate(line):
                if elem == '#':
                    temp_mask.add((x,y))
                elif elem == '>': # we know where the blizzard is at each time step, exlude #s
                    temp_mask.add((1+(x+time-1)%width, y))
                elif elem == '<':
                    temp_mask.add((1+(x-time-1)%width, y))
                elif elem == '^': # y is the index into the rows, so up is -1
                    temp_mask.add((x,1+(y-time-1)%height))
                elif elem == 'v':
                    temp_mask.add((x,1+(y+time-1)%height))
        ret.append(temp_mask)
    return ret

def get_neighbors(point, mask):
    x,y = point
    ret = []
    if (x,y) not in mask:
        ret.append((x,y))
    if (x+1,y) not in mask:
        ret.append((x+1,y))
    if (x-1,y) not in mask:
        ret.append((x-1,y))
    if (x,y+1) not in mask:
        ret.append((x,y+1))
    if (x,y-1) not in mask:
        ret.append((x,y-1))
    return ret

# BFS
# def run(start,end,board,masks: List[Set[Tuple[int,int]]], start_time=0):
#     x,y = start
#     queue = [(start_time,x,y)]

#     width = len(board[0])
#     height = len(board)
#     mask_n = (width-2)*(height-2) - 1

#     candidates = []
#     visited = set()
#     while queue:
#         time,x,y = queue.pop(0)

#         if (x < 0 or x >= width) or (y < 0 or y >= height) or board[y][x] == '#':
#             continue
#         if (time,x,y) in visited:
#             continue
#         visited.add((time,x,y))
#         if (x,y) == end:
#             candidates.append(time)
#             return time
#         for x_neighbor,y_neighbor in get_neighbors((x,y),masks[(time+1)%mask_n]):
#             queue.append((time+1,x_neighbor,y_neighbor))
#     return min(candidates)

# with open("input.txt", "r") as f:
#     data = f.read().split("\n")[:-1]


#     masks = create_graph_masks(data)
#     start = (data[0].index('.'),0)
#     end = (data[-1].index('.'),len(data)-1)
#     ans = run(start,end,data,masks)

#     print(ans)
def run(start,end,board,masks: List[Set[Tuple[int,int]]]):
    x,y = start
    end_visited = False
    start_visited_again = False
    queue = [(0,x,y,end_visited,start_visited_again)]

    width = len(board[0])
    height = len(board)
    mask_n = (width-2)*(height-2) - 1

    candidates = []
    visited = set()
    
    while queue:
        state = queue.pop(0)
        time,x,y,end_visited,start_visited_again = state

        if (x < 0 or x >= width) or (y < 0 or y >= height) or board[y][x] == '#':
            continue
        if (x,y) == end and start_visited_again and end_visited:
            return time
        if (x,y) == start and end_visited:
            start_visited_again = True
        if (x,y) == end:
            end_visited = True
        if (time,x,y,end_visited,start_visited_again) in visited:
            continue
        visited.add((time,x,y,end_visited,start_visited_again))
        
        for x_neighbor,y_neighbor in get_neighbors((x,y),masks[(time+1)%mask_n]):
            queue.append((time+1,x_neighbor,y_neighbor,end_visited,start_visited_again))
    return min(candidates)

with open("input.txt", "r") as f:
    data = f.read().split("\n")[:-1]


    masks = create_graph_masks(data)
    start = (data[0].index('.'),0)
    end = (data[-1].index('.'),len(data)-1)
    ans = run(start,end,data,masks)
    print(ans)