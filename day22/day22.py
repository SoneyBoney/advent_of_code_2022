

def get_first_nonspace(line: str):
    for i,c in enumerate(line):
        if c != ' ':
            return i
    raise RuntimeError('get_first_nonspace')

def get_last_nonspace(line: str):
    for i in range(len(line)-1, -1, -1):
        if line[i] != ' ':
            return i
    raise RuntimeError('get_last_nonspace')

def get_first_nonspace_y(board, x):
    for i,line in enumerate(board):
        if line[x] != ' ':
            return i
    raise RuntimeError('get_first_nonspace_y')

def get_last_nonspace_y(board, x):
    for i in range(len(board)-1,-1,-1):
        if board[i][x] != ' ':
            return i
    raise RuntimeError('get_last_nonspace_y')

class Player:
    def __init__(self, start):
        self.pos = start
        self.dir = 'right'

    def __repr__(self):
        return f'<Player at {self.pos} facing {self.dir}>'

    def move_forward(self, board):
        if self.dir == 'right':
            unit_step = (1,0)
        elif self.dir == 'left':
            unit_step = (-1,0)
        elif self.dir == 'up':
            unit_step = (0,-1)
        elif self.dir == 'down':
            unit_step = (0,1)
        else:
            raise RuntimeError(f'{self.dir} unknown dir')
        x_step,y_step = unit_step
        width = len(board[0])
        height = len(board)

        x,y = self.pos
        next_x,next_y = (x+x_step,y+y_step)

        if next_x >= width:
            next_x = 0
        if next_x < 0:
            next_x = width - 1
        if next_y >= height:
            next_y = 0
        if next_y < 0:
            next_y = height - 1

        while board[next_y][next_x] == ' ':
            next_x,next_y = (next_x+x_step,next_y+y_step)
            if next_x >= width:
                next_x = 0
            if next_x < 0:
                next_x = width - 1
            if next_y >= height:
                next_y = 0
            if next_y < 0:
                next_y = height - 1

        if board[next_y][next_x] != '#':
            self.pos = (next_x,next_y)
        

    def change_dir(self, dir: str):
        dir_map = ['up','right','down','left']
        dir_ind = dir_map.index(self.dir)
        if dir == 'R':
            new_ind = (dir_ind + 1) % 4
        if dir == 'L':
            new_ind = (dir_ind - 1) % 4
        self.dir = dir_map[new_ind]

def get_next_token(line: str):
    ret = []
    for i in range(len(line)):
        if not line[i].isnumeric():
            yield line[i]
        else:
            ret.append(line[i])
            try:
                if not line[i+1].isnumeric():
                    yield ''.join(ret)
                    ret = []
            except IndexError:
                yield ''.join(ret)

def square_board(board):
    max_len = max([len(x) for x in board])
    print(max_len)
    ret = []
    for line in board:
        num_padding = max_len - len(line)
        print(num_padding)
        padding = ' '*num_padding
        ret.append(line+padding)
    return ret

# with open("input.txt", "r") as f:
#     data = f.read().split("\n\n")

#     board_temp,desc_temp = data
#     board = board_temp.split('\n')
#     board = square_board(board)
#     import pprint
#     pprint.pprint(board)
#     desc = desc_temp.strip('\n')

#     start = board[0].index('.')
#     print(start)
#     player = Player((start,0))
#     for token in get_next_token(desc):
#         #print(player)
#         if token.isnumeric():
#             for _ in range(int(token)):
#                 player.move_forward(board)
#         else:
#             player.change_dir(token)
        

#     print(player)
#     facing_map = {'right':0, 'down':1,'left':2, 'up':3}
#     ans = 1000*(player.pos[1]+1) + 4*(player.pos[0]+1) + facing_map[player.dir]
#     print(ans)


# Idea: precompute all the (point,dir) -> (new_point,new_dir)
## map: (region,dir) -> (region,dir)
from typing import Tuple, Optional
def get_other_point(point: Tuple[int,int], dir) -> Tuple[int]:
    x,y = point
    if dir == 'U' and 50 <= x <= 99 and y == 0:
        return (0,150+x-50)
    if dir == 'L' and x == 0 and 150 <= y <= 199:
        return (y-150+50,0)
    if dir == 'U' and 100 <= x <= 149 and y == 0:
        return ()




with open("input.txt", "r") as f:
    data = f.read().split("\n\n")

    board_temp,desc_temp = data
    board = board_temp.split('\n')
    board = square_board(board)
    import pprint
    pprint.pprint(board)
    desc = desc_temp.strip('\n')

    start = board[0].index('.')
    
    print(start)
    player = Player((start,0))
    for token in get_next_token(desc):
        #print(player)
        if token.isnumeric():
            for _ in range(int(token)):
                player.move_forward(board)
        else:
            player.change_dir(token)
        

    print(player)
    facing_map = {'right':0, 'down':1,'left':2, 'up':3}
    ans = 1000*(player.pos[1]+1) + 4*(player.pos[0]+1) + facing_map[player.dir]
    print(ans)