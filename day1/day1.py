
with open('input.txt','r') as f:
    data = f.read().split('\n\n')
    datas = [d.strip('\n').split('\n') for d in data]
    ans = [sum([int(x) for x in a]) for a in datas]
    print(max(ans))
    print(sum(sorted(ans,reverse=True)[:3]))