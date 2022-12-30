

class DoublyLinkedList:
    def __init__(self, n:int):
        self.n = n
        self.prev = None
        self.next = None
        self.seen = False

    def __repr__(self):
        return f'<LL: n = {self.n}>'

def solve(num_list, part = 1):
    num_list = [DoublyLinkedList(n) for n in num_list]
    for i in range(len(num_list)-1):
        num_list[i].next = num_list[i+1]
        num_list[i+1].prev = num_list[i]
    num_list[-1].next = num_list[0]
    num_list[0].prev = num_list[-1]

    N = len(num_list) - 1
    for _ in range(10 if part == 2 else 0):
        for node in num_list:
            if node.n == 0:
                zero_head = node
                continue
            # head is now the next one to be moved
            find = node
            
            if node.n < 0:
                skip_num = -node.n % N
                for k in range(skip_num):
                    find = find.prev
                # head goes before find
                if node == find:
                    continue
                node.prev.next = node.next
                node.next.prev = node.prev
                find.prev.next = node
                node.prev = find.prev
                find.prev = node
                node.next = find
            else:
                skip_num = node.n % N
                for k in range(skip_num):
                    find = find.next
                # head goes after find
                if node == find:
                    continue
                node.next.prev = node.prev
                node.prev.next = node.next
                find.next.prev = node
                node.next = find.next
                find.next = node
                node.prev = find
            

    one_k = 1000 % len(num_list)
    two_k = 2000 % len(num_list)
    three_k = 3000 % len(num_list)
    nn = max(one_k,two_k,three_k)
    print(one_k,two_k,three_k)
    temp = zero_head

    ret = [None for _ in range(3)]
    for j in range(nn+1):
        if j == one_k:
            ret[0] = temp.n
        if j == two_k:
            ret[1] = temp.n
        if j == three_k:
            ret[2] = temp.n
        temp = temp.next
    return ret

# with open("input.txt", "r") as f:
#     data = f.read().split("\n")[:-1]

#     num_list = list(map(int,data))


#     ret = solve(num_list)
#     print(ret)
#     print(sum(ret))
with open("input.txt", "r") as f:
    data = f.read().split("\n")[:-1]

    num_list = list(map(int,data))
    num_list = [811589153*x for x in num_list]
    ret = solve(num_list, 2)
    print(ret)
    print(sum(ret))