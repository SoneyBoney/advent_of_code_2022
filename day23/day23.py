
class Elf:
    def __init__(self, cord):
        self.cord = cord
        self.prop = None
    
    def __repr__(self):
        return f'<Elf at {self.cord} with prop {self.prop}'

    def propose(self,board, dir_index):
        x,y = self.cord
        N = (x,y+1)
        E = (x+1,y)
        S = (x,y-1)
        W = (x-1,y)
        NE = (x+1,y+1)
        NW = (x-1,y+1)
        SE = (x+1,y-1)
        SW = (x-1,y-1)
        if not board.intersection(set([N,S,E,W,NE,NW,SE,SW])):
            self.prop = None
            return
        dirs = [(N,set([N,NE,NW])),(S,set([S,SE,SW])),(W,set([W,NW,SW])),(E,set([E,NE,SE]))]
        for i in range(dir_index,dir_index+4):
            step,check = dirs[i % 4]
            if not board.intersection(check):
                self.prop = step
                #print(f'{self} taking dir: ', i % 4)
                return
        #raise RuntimeError(f'{self} has no valid moves')
        self.prop = None 
        return
    
    def update_cord(self, move_counts):
        if self.prop is not None and move_counts[self.prop] == 1:
            self.cord = self.prop
            self.prop = None
            
def print_board(board):
    min_x = min([x for (x,y) in board])
    max_x = max([x for (x,y) in board])
    min_y = min([y for (x,y) in board])
    max_y = max([y for (x,y) in board])
    ret = []
    for y in range(max_y,min_y-1,-1):
        temp = []
        for x in range(min_x,max_x+1):
            if (x,y) in board:
                temp.append('#')
            else:
                temp.append('.')
        ret.append(''.join(temp))

    print('\n'.join(ret))

def get_empties(coords):
    min_x = min([x for (x,y) in coords])
    max_x = max([x for (x,y) in coords])
    min_y = min([y for (x,y) in coords])
    max_y = max([y for (x,y) in coords])
    print(min_x,max_x,min_y,max_y)
    x_len = max_x - (min_x-1)
    y_len = max_y - (min_y-1)
    area = x_len * y_len
    return area - len(coords)

def solve(elves,board):
    dir_index = 0
    for k in range(10000):
        #print(k)
        #print_board(board)
        move_counts = {}
        for elf in elves:
            elf.propose(board, dir_index)
            if elf.prop in move_counts.keys():
                move_counts[elf.prop] += 1
            else:
                move_counts[elf.prop] = 1
        #max_y_elf = max([e for e in elves if e.prop is not None],key=lambda x: x.prop)
        #print(max_y_elf)
        #print(move_counts)
        #print(f'Prop {k}')
        #print_board([x.prop for x in elves if x.prop is not None])
        for elf in elves:
            elf.update_cord(move_counts)
        #print(elves)
        if board == set([x.cord for x in elves]):
            print(k+1)
            exit('Process terminated')
        board = set([x.cord for x in elves])
        dir_index = (dir_index+1) % 4

    return get_empties([x.cord for x in elves])


with open("input.txt", "r") as f:
    data = f.read().split("\n")[:-1]

    elves = []
    y_cord = 0
    for line in data:
        for x,c in enumerate(line):
            if c == '#':
                elves.append(Elf((x,y_cord)))
        y_cord -= 1

    board = set([x.cord for x in elves])
    ret = solve(elves,board)
    print(ret)