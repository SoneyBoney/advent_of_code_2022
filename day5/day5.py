# with open('input.txt','r') as f:
#     data = f.read().split('\n')[:-1]
#     # 2 +3k, 9 lines, 10th is empty
#     pile = [[] for _ in range(9)]
#     for row in data[:8]:
#         for i in range(9):
#             index = 1+4*i
#             if row[index] != ' ':
#                 pile[i].append(row[index])
#     for instruction in data[10:]:
#         temp = instruction.split(' ')
#         num = int(temp[1])
#         from_num = int(temp[3])
#         to_num = int(temp[5])
#         for _ in range(num):
#             temp2 = pile[from_num-1].pop(0)
#             pile[to_num-1].insert(0,temp2)
#     ans = [x[0] for x in pile]
#     print(''.join(ans))

with open('input.txt','r') as f:
    data = f.read().split('\n')[:-1]
    # 2 +3k, 9 lines, 10th is empty
    pile = [[] for _ in range(9)]
    for row in data[:8]:
        for i in range(9):
            index = 1+4*i
            if row[index] != ' ':
                pile[i].append(row[index])
    for instruction in data[10:]:
        temp = instruction.split(' ')
        num = int(temp[1])
        from_num = int(temp[3])
        to_num = int(temp[5])
        temp2 = []
        for _ in range(num):
            temp2.append(pile[from_num-1].pop(0))

        pile[to_num-1] = temp2 + pile[to_num-1]
    ans = [x[0] for x in pile]
    print(''.join(ans))