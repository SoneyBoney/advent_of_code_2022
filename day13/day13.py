
import json
from enum import Enum

class Compare(Enum):
    RIGHT = 1
    WRONG = 2
    CONTINUE = 3



def compare(a, b):
    if isinstance(a,int) and isinstance(b,int):
        if a < b:
            return Compare.RIGHT
        elif a > b:
            return Compare.WRONG
        else:
            return Compare.CONTINUE
    elif isinstance(a,list) and isinstance(b,list):
        for a1,b1 in zip(a,b):
            temp = compare(a1,b1)
            if temp != Compare.CONTINUE:
                return temp
        if len(a) < len(b):
            return Compare.RIGHT
        elif len(a) > len(b):
            return Compare.WRONG
        else:
            return Compare.CONTINUE
    elif isinstance(a,int) and isinstance(b,list):
        return compare([a], b)
    elif isinstance(a,list) and isinstance(b,int):
        return compare(a, [b])
    else:
        raise RuntimeError('this aint a thing')

# with open('input.txt','r') as f:
#     data = f.read().split('\n\n')
#     print(data)
#     total = 0
#     for k,pair in enumerate(data):
#         try:
#             a,b = pair.strip('\n').split('\n')
#         except:
#             print('+++++++++++++++')
#             print(pair)
#             exit()
#         a = json.loads(a)
#         b = json.loads(b)
#         temp2 = compare(a,b)
#         if temp2 == Compare.RIGHT:
#             total += 1+k
#     print(total)

def wrapper(a,b):
    ret = compare(a,b)
    if ret == Compare.RIGHT:
        return -1
    if ret == Compare.WRONG:
        return 1
    else:
        return 0
import functools
with open('input.txt','r') as f:
    data = [json.loads(y) for y in [x for x in f.read().strip('\n').split('\n') if x]]
    data.append([[2]])
    data.append([[6]])
    
    ret = sorted(data, key=functools.cmp_to_key(wrapper))
    one = ret.index([[2]])+1
    two = ret.index([[6]])+1
    print(one*two)