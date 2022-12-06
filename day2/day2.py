
# opp_to_me = {'A': 'X', 'B': 'Y', 'C':'Z'}

# def get_score(opp, me):
#     opp = opp_to_me[opp]
#     if me == 'X':
#         me_pt = 1
#     elif me == 'Y':
#         me_pt = 2
#     elif me == 'Z':
#         me_pt = 3
#     else:
#         raise RuntimeError('fuck')
#     if me == opp:
#         return 3+me_pt
#     if (opp,me) == ('X','Y'):
#         return me_pt + 6
#     if (opp,me) == ('Y','Z'):
#         return me_pt +6
#     if (opp,me) == ('Z','X'):
#         return me_pt +6
#     return me_pt

# with open('input.txt','r') as f:
#     data = f.read().split('\n')[:-1]
#     temp = [get_score(x[0],x[2]) for x in data]
#     ans = sum(temp)
#     print(ans)

op_lose = {'A': 2, 'B':3, 'C':1}
op_win = {'A': 3, 'B':1, 'C':2}
draw = {'A': 1, 'B':2, 'C':3}
def two(op,me):
    if me == 'X':
        return op_win[op]
    if me =='Y':
        return draw[op]
    return op_lose[op]
me_to_score = {'X': 0, 'Y':3, 'Z':6}
with open('input.txt','r') as f:
    data = f.read().split('\n')[:-1]
    temp = [two(x[0],x[2])+me_to_score[x[2]] for x in data]
    ans = sum(temp)
    print(ans)
