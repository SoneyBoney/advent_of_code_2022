# from typing import Tuple
# import math
# from pprint import pprint

# # Wrapper to pass object around since worry levels may not be unique
# # actually it probably doens't matter but ok
# class Item:
#     def __init__(self, worry: int):
#         self.worry = worry

#     def __repr__(self):
#         return f'Item: {self.worry}'
        


# class Monkey:
#     def __init__(self, num: int, starting_items: list[int], update_rule, throw_rule):
#         self.num = num
#         self.items = [Item(it) for it in starting_items]
#         if update_rule[1] == '*':
#             self.update_rule = lambda x: ((x if update_rule[0] == 'old' else int(update_rule[0])) * (x if update_rule[2] == 'old' else int(update_rule[2])))
#         elif update_rule[1] == '+':
#             self.update_rule = lambda x: ((x if update_rule[0]=='old' else int(update_rule[0])) + (x if update_rule[2]=='old' else int(update_rule[2])))
#         #self.update_rule = update_rule
#         self.throw_rule = throw_rule
#         self.total_inspected = 0

#     def choose_monkey(self) -> Tuple[int, Item]:
#         current_item = self.items.pop(0)
#         self.total_inspected += 1
#         new_worry = self.update_rule(current_item.worry)
#         divided_worry = math.floor(new_worry / 3)
#         to_monkey = self.throw_rule(divided_worry)
#         current_item.worry = divided_worry
#         return to_monkey, current_item
    
#     def __repr__(self):
#         return f'<Monkey: {self.num} has items: {self.items}'
        
# def parse_block(block: str) -> Monkey:
#     rule_parts = block.split('\n')
#     monkey_num = int(rule_parts[0].split(' ')[1][:-1])
#     starting_items = [int(x) for x in rule_parts[1].strip(' ').split('Starting items:')[1:][0].strip().split(',')]
#     update_rule = rule_parts[2].strip(' ').split('Operation: new =')[1].split()
    
#     divisor = int(rule_parts[3].strip(' ').split(' ')[-1])
#     true_monkey = int(rule_parts[4].strip(' ').split(' ')[-1])
#     false_monkey = int(rule_parts[5].strip(' ').split(' ')[-1])
#     test_rule = lambda y: true_monkey if (y % divisor) == 0 else false_monkey
#     return Monkey(monkey_num, starting_items, update_rule, test_rule)


# with open('input.txt','r') as f:
#     data = f.read().split('\n\n')
#     num_monkeys = len(data)
#     monkeys = [None for _ in range(num_monkeys)]
#     for block in data:
#         this_monkey = parse_block(block)
#         monkeys[this_monkey.num] = this_monkey

#     for round in range(20):
#         for monkey in monkeys:
#             while monkey.items:
#                 to_monkey,item = monkey.choose_monkey()
#                 monkeys[to_monkey].items.append(item)
#         print('ROUND: ',round)
#         pprint(monkeys)
#     ans = sorted([x.total_inspected for x in monkeys])
#     print(ans[-1]* ans[-2])
#     print()

from typing import Tuple
import math
from pprint import pprint

# Wrapper to pass object around since worry levels may not be unique
# actually it probably doens't matter but ok
class Item:
    def __init__(self, worry: int):
        self.worry = worry

    def __repr__(self):
        return f'Item: {self.worry}'
        


class Monkey:
    def __init__(self, num: int, starting_items: list[int], update_rule, throw_rule):
        self.num = num
        self.items = [Item(it) for it in starting_items]
        if update_rule[1] == '*':
            self.update_rule = lambda x: ((x if update_rule[0] == 'old' else int(update_rule[0])) * (x if update_rule[2] == 'old' else int(update_rule[2])))
        elif update_rule[1] == '+':
            self.update_rule = lambda x: ((x if update_rule[0]=='old' else int(update_rule[0])) + (x if update_rule[2]=='old' else int(update_rule[2])))
        #self.update_rule = update_rule
        self.throw_rule = throw_rule
        self.total_inspected = 0

    def choose_monkey(self) -> Tuple[int, Item]:
        current_item = self.items.pop(0)
        self.total_inspected += 1
        new_worry = self.update_rule(current_item.worry) % 9699690
        #divided_worry = math.floor(new_worry / 3)
        #modded_worry = new_worry % 104729
        to_monkey = self.throw_rule(new_worry)
        current_item.worry = new_worry
        return to_monkey, current_item
    
    def __repr__(self):
        return f'<Monkey: {self.num} has items: {self.items}'
        
def parse_block(block: str) -> Monkey:
    rule_parts = block.split('\n')
    monkey_num = int(rule_parts[0].split(' ')[1][:-1])
    starting_items = [int(x) for x in rule_parts[1].strip(' ').split('Starting items:')[1:][0].strip().split(',')]
    update_rule = rule_parts[2].strip(' ').split('Operation: new =')[1].split()
    
    divisor = int(rule_parts[3].strip(' ').split(' ')[-1])
    true_monkey = int(rule_parts[4].strip(' ').split(' ')[-1])
    false_monkey = int(rule_parts[5].strip(' ').split(' ')[-1])
    test_rule = lambda y: true_monkey if (y % divisor) == 0 else false_monkey
    return Monkey(monkey_num, starting_items, update_rule, test_rule)


with open('input.txt','r') as f:
    data = f.read().split('\n\n')
    num_monkeys = len(data)
    monkeys = [None for _ in range(num_monkeys)]
    for block in data:
        this_monkey = parse_block(block)
        monkeys[this_monkey.num] = this_monkey

    for round in range(10000):
        for monkey in monkeys:
            while monkey.items:
                to_monkey,item = monkey.choose_monkey()
                monkeys[to_monkey].items.append(item)
        
        # if round == 19:
        #     for monkey in monkeys:
        #         print(f'Monkey {monkey.num} inspected items {monkey.total_inspected} times')
        #     exit()

    ans = sorted([x.total_inspected for x in monkeys])
    print(ans[-1]* ans[-2])
    print()

