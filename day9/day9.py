
# import itertools
# with open('input.txt','r') as f:
#     data = f.read().split('\n')[:-1]

#     seen = set()
#     tail = (0,0)
#     head = (0,0)
#     seen.add(tail)
#     for move in data:
#         dir,steps = move.split(' ')
#         for i in range(int(steps)):
#             if dir == 'U':
#                 head = (head[0],head[1]+1)
#             if dir == 'D':
#                 head = (head[0],head[1]-1)
#             if dir == 'L':
#                 head = (head[0]-1,head[1])
#             if dir == 'R':
#                 head = (head[0]+1,head[1])
#             if abs(head[0]-tail[0]) <= 1 and abs(head[1]-tail[1]) <= 1:
#                 continue
#             else: # move tails
#                 # if it is 2 steps in some dir, go that dir. If not, go closest diag step to head
#                 two_steps = [   (tail[0]+2,tail[1]),
#                                 (tail[0]-2,tail[1]),
#                                 (tail[0],tail[1]+2),
#                                 (tail[0],tail[1]-2)
#                             ]
#                 if head in two_steps:
#                     if dir == 'U':
#                         tail = (tail[0],tail[1]+1)
#                     if dir == 'D':
#                         tail = (tail[0],tail[1]-1)
#                     if dir == 'L':
#                         tail = (tail[0]-1,tail[1])
#                     if dir == 'R':
#                         tail = (tail[0]+1,tail[1])
#                 else: # diag 
#                     diags = [   (tail[0]+1,tail[1]+1),
#                                 (tail[0]+1,tail[1]-1),
#                                 (tail[0]-1,tail[1]+1),
#                                 (tail[0]-1,tail[1]-1)
#                             ]
#                     tail = min(diags, key=lambda x: ((x[0]-head[0])**2+(x[1]-head[1])**2))
#                 seen.add(tail)
#     #print(seen)
#     print(len(seen))
 
def close_enuf(h,t):
    a = abs(h[0] - t[0]) == 1 and h[1] == t[1]
    b = abs(h[1] - t[1]) == 1 and h[0] == t[0]
    c = abs(h[0] - t[0]) == 1 and abs(h[1] - t[1]) == 1
    return h == t or a or b or c

example = '''R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20'''
import itertools
from pprint import pprint
with open('input.txt','r') as f:
    data = f.read().split('\n')[:-1]

    
    seen = set()
    last_dirs = [None for _ in range(10)]
    rope = [(0,0) for _ in range(10)]
    for move in data: #example.split('\n'):
        dir,steps = move.split(' ')
        last_dirs[0] = dir
        for _ in range(int(steps)):
            if dir == 'U':
                rope[0] = (rope[0][0],rope[0][1]+1)
            if dir == 'D':
                rope[0] = (rope[0][0],rope[0][1]-1)
            if dir == 'L':
                rope[0] = (rope[0][0]-1,rope[0][1])
            if dir == 'R':
                rope[0] = (rope[0][0]+1,rope[0][1])
            for i in range(9):
                seen.add(rope[-1])
                if abs(rope[i][0]-rope[i+1][0]) <= 1 and abs(rope[i][1]-rope[i+1][1]) <= 1:
                    continue
                else: # move tail
                    if rope[i][0] > rope[i+1][0]:
                        x = rope[i+1][0] + 1
                    if rope[i][0] < rope[i+1][0]:
                        x = rope[i+1][0] - 1
                    if rope[i][0] == rope[i+1][0]:
                        x = rope[i+1][0]
                    if rope[i][1] > rope[i+1][1]:
                        y = rope[i+1][1] + 1
                    if rope[i][1] < rope[i+1][1]:
                        y = rope[i+1][1] - 1
                    if rope[i][1] == rope[i+1][1]:
                        y = rope[i+1][1]
                    rope[i+1] = (x,y)
                    assert abs(rope[i][0]-rope[i+1][0]) <= 1 and abs(rope[i][1]-rope[i+1][1]) <= 1
    
                    
    print(len(seen))
 
#   # if it is 2 steps in some dir, go that dir. If not, go closest diag step to head
#                     two_steps = [   (rope[i+1][0]+2,rope[i+1][1]),
#                                     (rope[i+1][0]-2,rope[i+1][1]),
#                                     (rope[i+1][0],rope[i+1][1]+2),
#                                     (rope[i+1][0],rope[i+1][1]-2)
#                                 ]
#                     if rope[i] in two_steps and last_dirs[i] != 'DIAG':
#                         temp_dir = last_dirs[i]
#                         if temp_dir == 'U':
#                             rope[i+1] = (rope[i+1][0],rope[i+1][1]+1)
#                         if temp_dir == 'D':
#                             rope[i+1] = (rope[i+1][0],rope[i+1][1]-1)
#                         if temp_dir == 'L':
#                             rope[i+1] = (rope[i+1][0]-1,rope[i+1][1])
#                         if temp_dir == 'R':
#                             rope[i+1] = (rope[i+1][0]+1,rope[i+1][1])
#                         last_dirs[i+1] = temp_dir
#                     else: # diag 
#                         diags = [   (rope[i+1][0]+1,rope[i+1][1]+1),
#                                     (rope[i+1][0]+1,rope[i+1][1]-1),
#                                     (rope[i+1][0]-1,rope[i+1][1]+1),
#                                     (rope[i+1][0]-1,rope[i+1][1]-1)
#                                 ]
#                         print('before:')
#                         print(i,rope[i],i+1,rope[i+1])
#                         rope[i+1] = min(diags, key=lambda x: ((x[0]-rope[i][0])**2+(x[1]-rope[i][1])**2))
#                         if not(abs(rope[i][0]-rope[i+1][0]) <= 1 and abs(rope[i][1]-rope[i+1][1]) <= 1):
#                             print(i,rope[i],i+1,rope[i+1])
#                             print(diags)
#                             exit()
#                         print('after:')
#                         print(i,rope[i],i+1,rope[i+1])
#                         last_dirs[i+1] = 'DIAG'
#         #pprint(grid)