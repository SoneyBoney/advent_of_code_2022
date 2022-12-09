# class Tree:
#     def __init__(self, n):
#         self.n = n
#         self.left = None 
#         self.right = None
#         self.top = None
#         self.bot = None

#     def __repr__(self):
#         return f'{self.left}, {self.right}, {self.top}, {self.bot}'

# with open('input.txt','r') as f:
#     data = f.read().split('\n')[:-1]
#     n = len(data[0])
#     grid = []
#     for line in data:
#         temp = []
#         for str_n in line:
#             temp.append(Tree(int(str_n)))
#         grid.append(temp)
#     N = len(grid)
#     for j in range(1,N-1):
#         max_left = grid[j][0].n
#         max_right = grid[j][-1].n
#         max_top = grid[0][j].n
#         max_bot = grid[-1][j].n
#         for i in range(1,N-1):
#             if grid[j][i].n <= max_left:
#                 grid[j][i].left = True
#             if grid[j][i].n > max_left:
#                 max_left = grid[j][i].n
#             if grid[j][-(i+1)].n <= max_right:
#                 grid[j][-(i+1)].right = True 
#             if grid[j][-(i+1)].n > max_right:
#                 max_right = grid[j][-(i+1)].n
#             if grid[i][j].n <= max_top:
#                 grid[i][j].top = True 
#             if grid[i][j].n > max_top:
#                 max_top = grid[i][j].n
#             if grid[-(i+1)][j].n <= max_bot:
#                 grid[-(i+1)][j].bot = True 
#             if grid[-(i+1)][j].n > max_bot:
#                 max_bot = grid[-(i+1)][j].n

#     ans = 0
#     for row in grid:
#         for elem in row:
#             if not((elem.left) and (elem.right) and (elem.top) and (elem.bot)):
#                 ans += 1  
#     print(ans)

class Tree:
    def __init__(self, n):
        self.n = n
        self.left = 0 
        self.right = 0
        self.top = 0
        self.bot = 0

    def __repr__(self):
        return f'N = {self.n}\nLeft: {self.left}, Right: {self.right}, Top: {self.top}, Bot: {self.bot}'

with open('input.txt','r') as f:
    data = f.read().split('\n')[:-1]
    n = len(data[0])
    grid = []
    for line in data:
        temp = []
        for str_n in line:
            temp.append(Tree(int(str_n)))
        grid.append(temp)
    N = len(grid)
    for i in range(N):
        for j in range(N):
            for k in range(j+1,N):
                if grid[i][k].n >= grid[i][j].n or k == N-1:
                    grid[i][j].right = k - j
                    break
            for k in range(j-1,-1,-1):
                if grid[i][k].n >= grid[i][j].n or k == 0:
                    grid[i][j].left = j - k
                    break
            for k in range(i+1,N):
                if grid[k][j].n >= grid[i][j].n or k == N-1:
                    grid[i][j].bot = k - i
                    break
            for k in range(i-1,-1,-1):
                if grid[k][j].n >= grid[i][j].n or k == 0:
                    grid[i][j].top = i - k
                    break
    print(grid[1][N-49])

    ans = list(map(max,[[x.left*x.right*x.top*x.bot for x in xs] for xs in grid]))
    print(max(ans))