# with open('input.txt','r') as f:
#     data = f.read().split('\n')[0]


#     for i in range(len(data)-4):
#         temp = set()
#         temp.add(data[i])
#         temp.add(data[i+1])
#         temp.add(data[i+2])
#         temp.add(data[i+3])
#         if len(temp) == 4:
#             print(i+4)
#             break
with open('input.txt','r') as f:
    data = f.read().split('\n')[0]
    for i in range(len(data)-4):
        temp = set()
        temp.add(data[i])
        temp.add(data[i+1])
        temp.add(data[i+2])
        temp.add(data[i+3])
        temp.add(data[i+4])
        temp.add(data[i+5])
        temp.add(data[i+6])
        temp.add(data[i+7])
        temp.add(data[i+8])
        temp.add(data[i+9])
        temp.add(data[i+10])
        temp.add(data[i+11])
        temp.add(data[i+12])
        temp.add(data[i+13])
        if len(temp) == 14:
            print(i+14)
            break