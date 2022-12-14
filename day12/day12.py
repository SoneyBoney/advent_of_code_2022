import itertools as it
import heapq
import math

def walk_history(history, last):
    ret = []
    ret.append(last)
    while last in history.keys():
        last = history[last]
        ret.append(last)
    return ret

def l1_distance(x,y):
    return abs(x[0]-y[0]) + abs(x[1]-y[1])

def get_neighbors(cord, grid):
    h = len(grid)
    w = len(grid[0])
    current_level = ord(grid[cord[0]][cord[1]]) if grid[cord[0]][cord[1]] != 'S' else ord('a')
    neighbors = [(cord[0]+1,cord[1]),(cord[0]-1,cord[1]),(cord[0],cord[1]+1),(cord[0],cord[1]-1)]
    candidate_steps = [(x,y) for (x,y) in neighbors if 0 <= x < h and 0<=y<w]
    ret = [c for c in candidate_steps if (ord(grid[c[0]][c[1]])-current_level <= 1 and grid[c[0]][c[1]]!='E') or (grid[c[0]][c[1]]=='E' and ord('z')-current_level <= 1 )]

    return ret 

def a_star(start, end, grid):
    history = {}
    global_score = {(x,y):math.inf for (x,y) in it.product(*[range(len(grid)),range(len(grid[0]))])}
    local_score = {(x,y):math.inf for (x,y) in it.product(*[range(len(grid)),range(len(grid[0]))])}

    global_score[start] = 0
    local_score[start] = l1_distance(start,end)

    candidates = [(local_score[start],start)] 
    heapq.heapify(candidates)
    steps = 0
    while candidates:
        this_candidate = heapq.heappop(candidates)
        #print(this_candidate)
        this_candidate = this_candidate[1]
        if this_candidate == end:
            return walk_history(history,end)
        for neighbor in get_neighbors(this_candidate,grid):
            temp = global_score[this_candidate] + 1
            if temp < global_score[neighbor]:
                global_score[neighbor] = temp
                local_score[neighbor] = temp + l1_distance(neighbor,end)
                history[neighbor] = this_candidate
                if (local_score[neighbor],neighbor) not in candidates:
                    heapq.heappush(candidates, (local_score[neighbor],neighbor))

    #return global_score[end]



# with open('input.txt','r') as f:
#     data = f.read().split('\n')[:-1]

#     grid = [[c for c in line] for line in data]

#     for i,line in enumerate(grid):
#         for j,c in enumerate(line):
#             if c == 'S':
#                 start = (i,j)
#             elif c == 'E':
#                 end = (i,j)

#     ans = a_star(start,end,grid)

#     print(ans[::-1])
#     print(len(ans))
    #print(grid)

with open('input.txt','r') as f:
    data = f.read().split('\n')[:-1]

    grid = [[c for c in line] for line in data]
    starts = []
    for i,line in enumerate(grid):
        for j,c in enumerate(line):
            if c == 'S' or c == 'a':
                starts.append((i,j))
            elif c == 'E':
                end = (i,j)
    ans = math.inf
    for start in starts:
        temp = a_star(start,end,grid)
        if temp:
            ans = min(ans,len(temp)-1)
    print(ans)

