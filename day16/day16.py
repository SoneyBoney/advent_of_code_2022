import math
from typing import Dict, List, Tuple, Set

class Valve:
    def __init__(self, name: str, flow_rate: int, children: List[str]):
        self.name = name
        self.flow_rate = flow_rate
        self._children_str = children
        self.children = []

    def add_children(self, valve_dict: Dict[str, 'Valve']):
        for child in self._children_str:
            self.children.append(valve_dict[child])
        
    def __repr__(self):
        return f'<Valve {self.name} with flow {self.flow_rate}, children: {self._children_str}>'


def parse_valve(line: str) -> Valve:
    valve_name = line[6:8]
    children_str = [x.split(' ')[-1].strip() for x in line.split('to')[-1].strip().split(',')]
    flow_rate = int(line.split(';')[0].split('flow rate=')[-1])
    return Valve(valve_name, flow_rate, children_str)

def compute_key(time: int, node: Valve, seen):

    pass

def compute_scores(t: int, node: Valve, tablet: Dict, already_on):
    if t == 0:
        return 0
    key = (t,node.name,already_on)
    if key in tablet.keys():
        return tablet[key]
    ret = -1
    if node.flow_rate > 0 and node.name not in already_on:
        ret = ((t-1)*node.flow_rate) +compute_scores(t-1,node,tablet,already_on.union(frozenset([node.name])))
    
    for child in node.children:
        ret = max(ret,compute_scores(t-1,child,tablet,already_on))
    
    tablet[key] = ret 
    return ret

with open("input.txt", "r") as f:
    data = f.read().split("\n")[:-1]

    valve_dict = {}
    for i,line in enumerate(data):
        temp_valv = parse_valve(line)
        valve_dict[temp_valv.name] = temp_valv
    for v in valve_dict.values():
        for child in v._children_str:
            v.children.append(valve_dict[child])
    
    
    ret = compute_scores(30, valve_dict['AA'], {}, frozenset())
    print(ret)
