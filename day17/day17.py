
class Shape:
    def __init__(self, type: int, height: int):
        if type == 0:
            self.points = [(x,height) for x in range(2,6)]
        elif type == 1:
            self.points = [(3,height),(2,height+1),(3,height+1),(4,height+1),(3,height+2)]
        elif type == 2:
            self.points = [(2,height),(3,height),(4,height),(4,height+1),(4,height+2)]
        elif type == 3:
            self.points = [(2,height+y) for y in range(4)]
        elif type == 4:
            self.points = [(2,height), (3,height), (2,height+1), (3,height+1)]

    def push_shape(self, dir: str, board):
        new_points = []
        for p in self.points:
            new_x = p[0] - 1 if dir == "<" else p[0] + 1
            if new_x < 0 or new_x > 6 or (new_x, p[1]) in board:
                return
            new_points.append((new_x, p[1]))
        self.points = new_points

    def drop_shape(self, board):
        new_points = [(p[0],p[1]-1) for p in self.points]
        if board.intersection(set(new_points)):
            return True
        self.points = new_points
        return False


def print_board(board):
    max_height = max([y for (x,y) in board]) +1
    temp = [['.' for _ in range(7)] for _ in range(max_height)]
    for (x,y) in board:
        temp[y][x] = '#'
        
    print('\n'.join([''.join(temp1) for temp1 in temp][::-1]))

def approx_board_state(board):
    max_height = max([y for (x,y) in board])
    return frozenset([(x,max_height-y) for (x,y) in board if max_height-y<=6])

def simulate(jet_stream: str, epoch: int):
    ret = 0
    current_max_height = 0
    counter = 0
    board = set([(x,0) for x in range(7)])
    period_tracker = {}
    rock_num = 0
    periodic_accum = 0
    while rock_num < epoch:
        
        rock = Shape(rock_num % 5,current_max_height+4)
        while True:
            dir = jet_stream[counter]
            counter = (counter + 1) % len(jet_stream)
            #print(dir)
            rock.push_shape(dir,board)
            is_stopped = rock.drop_shape(board)
            if is_stopped:
                for p in rock.points:
                    board.add(p)
                current_max_height = max(current_max_height,max([y for (x,y) in rock.points]))
                break
            
        key = (rock_num % 5, counter, approx_board_state(board))
        if key in period_tracker.keys():
            old_rock_num, old_max_height = period_tracker[key]
            strides_left = (epoch - rock_num) // (rock_num - old_rock_num)
            periodic_accum += (current_max_height - old_max_height) * strides_left
            rock_num += strides_left * (rock_num - old_rock_num)
            if strides_left:
                print(strides_left,old_rock_num,old_max_height)
        period_tracker[key] = rock_num,current_max_height
        rock_num += 1
    print(periodic_accum)
    return current_max_height + periodic_accum

with open("input.txt", "r") as f:
    data = f.read().split("\n")[:-1]

    #ret = simulate(data[0],2022)
    ret = simulate(data[0],1000000000000)
    print(ret)