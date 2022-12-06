# with open('input.txt','r') as f:
#     data = f.read().split('\n')[:-1]
#     ret = 0
#     for x in data:
#         first,second = x.split(',')
#         first_low,first_high = [int(d) for d in first.split('-')]
#         second_low,second_high = [int(d) for d in second.split('-')]
#         print(first_low,first_high)
#         print(second_low,second_high)
#         if first_low <= second_low and first_high >= second_high:
#             ret += 1
#         elif first_low >= second_low and first_high <= second_high:
#             ret += 1
#     print(ret)

with open('input.txt','r') as f:
    data = f.read().split('\n')[:-1]
    ret = 0
    for x in data:
        first,second = x.split(',')
        first_low,first_high = [int(d) for d in first.split('-')]
        second_low,second_high = [int(d) for d in second.split('-')]

        if first_high >= second_low and second_high >= first_low:
            ret += 1
        elif second_high >= first_low and second_low <= first_high:
            ret += 1
    print(ret)