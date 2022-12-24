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

def compute_scores(t: int, node: Valve, current_score: int, tablet: List[Dict[str,Valve]], already_on: Set[Valve]):
    #print(t, node.name, current_score)
    if t == 0:
        return
    if current_score >= tablet[t-1][node.name]:
        tablet[t-1][node.name] = current_score
    else:
        return

    if node.name not in already_on:
            compute_scores(t-1, node, current_score+((t-1)*node.flow_rate), tablet, already_on.union(set([node.name])))

    for child in node.children:
        compute_scores(t-1, child, current_score, tablet, already_on)


def walk_tablet(tablet):
    ret = []
    for step in tablet[::-1]:
        ret.append(max([y for y in step.items()],key=lambda x: x[1]))
    return ret
# 1627, 1615
with open("test.txt", "r") as f:
    data = f.read().split("\n")[:-1]

    valve_dict = {}
    for i,line in enumerate(data):
        temp_valv = parse_valve(line)
        valve_dict[temp_valv.name] = temp_valv
    for v in valve_dict.values():
        v.add_children(valve_dict)
    
    tablet = [{ valve_name : 0 for valve_name in valve_dict.keys()} for _ in range(30)]
    ret = compute_scores(30,valve_dict['AA'],0,tablet, set())
    
    from pprint import pprint
    
    pprint(walk_tablet(tablet))

    print(ret)