
# with open('input.txt','r') as f:
#     data = f.read().split('\n')[:-1]
#     temp0 = list((map(lambda x: set(x[:len(x)//2]).intersection(set(x[len(x)//2:])), data)))
#     print(temp0)
#     temp1 = list(map(lambda y: ord(list(y)[0])-ord('A')+27 if list(y)[0].isupper() else ord(list(y)[0])-ord('a')+1,temp0))
#     print(list(temp1))
#     print(sum(temp1))

with open('input.txt','r') as f:
    data = f.read().split('\n')[:-1]
    poo = []
    for i in range(0,len(data),3):
        temp = set(data[i]).intersection(set(data[i+1])).intersection(set(data[i+2]))
        poo.append(list(temp)[0])
    temp1 = list(map(lambda y: ord(list(y)[0])-ord('A')+27 if list(y)[0].isupper() else ord(list(y)[0])-ord('a')+1,poo))
    print(sum(temp1))
        