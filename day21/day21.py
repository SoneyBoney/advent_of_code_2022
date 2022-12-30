
class Expr:
    def __init__(self, is_num, expr):
        self.is_num = is_num
        if is_num:
            self.expr = int(expr)
        else:
            self.expr = expr.split(' ')

def parse_expression(line: str):
    this_var,expr = line.split(':')
    expr = expr.strip()
    return this_var,Expr(expr.isnumeric(),expr)

# def eval(varname, store):
#     expr = store[varname]
#     if expr.is_num: #isinstance(expr,(int, float)):
#         return expr.expr
#     first_arg,op,second_arg = expr.expr
#     if op == '+':
#         return eval(first_arg,store) + eval(second_arg,store)
#     if op == '-':
#         return eval(first_arg,store) - eval(second_arg,store)
#     if op == '*':
#         return eval(first_arg,store) * eval(second_arg,store)
#     if op == '/':
#         return eval(first_arg,store) / eval(second_arg,store)

# with open("input.txt", "r") as f:
#     data = f.read().split("\n")[:-1]
#     print(data)
#     store = {}
#     for line in data:
#         varname, expr = parse_expression(line)
#         store[varname] = expr
#     ret = eval('root',store)
#     print(ret)
def eval(varname, store):
    expr = store[varname]
    if expr.is_num: 
        return expr.expr
    first_arg,op,second_arg = expr.expr
    if op == '+':
        return eval(first_arg,store) + eval(second_arg,store)
    if op == '-':
        return eval(first_arg,store) - eval(second_arg,store)
    if op == '*':
        return eval(first_arg,store) * eval(second_arg,store)
    if op == '/':
        return eval(first_arg,store) / eval(second_arg,store)

with open("input.txt", "r") as f:
    data = f.read().split("\n")[:-1]
    print(data)
    store = {}
    for line in data:
        varname, expr = parse_expression(line)
        store[varname] = expr

    arg1,_,arg2 = store['root'].expr

    store['humn'] = Expr(True,1)
    ans1 = eval(arg1,store)
    ans2 = eval(arg2,store)
    print(ans1-ans2)

    store['humn'] = Expr(True,2)
    ans11 = eval(arg1,store)
    print(ans11-ans2)

    store['humn'] = Expr(True,3)
    ans111 = eval(arg1,store)
    print(ans111-ans2)

    print(ans1-ans11,ans11-ans111)

    store['humn'] = Expr(True,4)
    ans1111 = eval(arg1,store)
    print(ans111-ans1111)

    store['humn'] = Expr(True,3451534022348)
    ans11111 = eval(arg1,store)
    print(ans11111-ans2)