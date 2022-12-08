
# class Treee:
#     def __init__(self, name):
#         self.name = name
#         self.files = {}
#         self.children = {}
            
    
# global_sum = 0
# def get_ans(treee):
#     total_filesize = sum(treee.files.values())
#     for c in treee.children.values():
#         total_filesize += get_ans(c)
#     if total_filesize <= 100000:
#         global global_sum
#         global_sum += total_filesize
#     return total_filesize
    

# with open('input.txt','r') as f:
#     data = f.read().split('\n')[:-1]

#     stack = []
#     dir = None
#     root = None
#     for cmd in data:
#         if cmd[0] == '$':
#             if cmd.split(' ')[1] == 'cd':
#                 #print([x.name for x in stack])
                
#                 dirname = cmd.split(' ')[2]
#                 if dirname == '..':
#                     dir = stack.pop(0)
#                 else:
#                     if dir:
#                         stack.insert(0,dir)
#                     temp_dir = Treee(dirname)
#                     if dir:
#                         dir.children[dirname] = temp_dir
#                     else:
#                         root = temp_dir
#                     dir = temp_dir
#         elif cmd.split(' ')[0].isnumeric():
#             filename = cmd.split(' ')[1]
#             filesize = int(cmd.split(' ')[0])
#             dir.files[filename] = filesize

#     ans = get_ans(root)
#     print(global_sum)


class Treee:
    def __init__(self, name):
        self.name = name
        self.files = {}
        self.children = {}
            
    
global_list = []
def get_ans(treee):
    total_filesize = sum(treee.files.values())
    for c in treee.children.values():
        total_filesize += get_ans(c)
    global global_list
    global_list.append(total_filesize)
    return total_filesize
    

with open('input.txt','r') as f:
    data = f.read().split('\n')[:-1]

    stack = []
    dir = None
    root = None
    for cmd in data:
        if cmd[0] == '$':
            if cmd.split(' ')[1] == 'cd':
                #print([x.name for x in stack])
                
                dirname = cmd.split(' ')[2]
                if dirname == '..':
                    dir = stack.pop(0)
                else:
                    if dir:
                        stack.insert(0,dir)
                    temp_dir = Treee(dirname)
                    if dir:
                        dir.children[dirname] = temp_dir
                    else:
                        root = temp_dir
                    dir = temp_dir
        elif cmd.split(' ')[0].isnumeric():
            filename = cmd.split(' ')[1]
            filesize = int(cmd.split(' ')[0])
            dir.files[filename] = filesize

    total_used = get_ans(root)
    target = (total_used - 40000000)
    sorted_list = sorted(global_list)
    for n in sorted_list:
        if n >= target:
            print(n)
            break
