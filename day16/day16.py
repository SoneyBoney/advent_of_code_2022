from typing import Dict, List, Tuple

class Valve:
    def __init__(self, name: str, flow_rate: int, children: List[str]):
        self.name = name
        self.flow_rate = flow_rate
        self._children_str = children
        self.children = set()

    def add_children(self, valve_dict: Dict[str, 'Valve']):
        for child in self._children_str:
            self.children.add(valve_dict[child])
        
    def __repr__(self):
        return f'<Valve {self.name} with flow {self.flow_rate}, children: {self.children}>'


def parse_valve(line: str) -> Tuple[str,Valve]:
    valve_name = line[6:8]
    children_str = [x.strip() for x in line.split('tunnels lead to valves')[-1].strip().split(',')]
    exit()
    pass

with open("input.txt", "r") as f:
    data = f.read().split("\n")[:-1]

    valve_dict = {}
    for line in data:
        temp_name, temp_valv = parse_valve(line)