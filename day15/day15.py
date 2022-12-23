import re
from typing import Tuple, List
import multiprocessing as mp

def l1_distance(x: Tuple[int,int], y: Tuple[int,int]):
    return abs(x[0]-y[0]) + abs(x[1]-y[1])

class Sensor:
    def __init__(self, position: Tuple[int,int], closest_beacon: Tuple[int,int]):
        self.position = position
        self.closest_beacon = closest_beacon
        self.min_distance = l1_distance(position, closest_beacon)

    def __repr__(self):
        return f'<Sensor at: {self.position} with min_distance: {self.min_distance}>'

def is_within_sensor(position: Tuple[int,int], sensor: Sensor):
    if l1_distance(position, sensor.position) <= sensor.min_distance:
        return True
    else:
        return False

def parse_sensor(line: str):
    temp = line.split(':')
    sensor_x = int(re.search(r'x=.*,', temp[0]).group(0)[2:-1])
    sensor_y = int(re.search(r'y=.*', temp[0]).group(0)[2:])
    beacon_x = int(re.search(r'x=.*,', temp[1]).group(0)[2:-1])
    beacon_y = int(re.search(r'y=.*', temp[1]).group(0)[2:])
    return Sensor(position=(sensor_x,sensor_y),closest_beacon=(beacon_x,beacon_y))

def process_ranges(x_min: int, x_max: int, y: int, sensors: List[Sensor], beacons):
    ret = 0
    for x in range(x_min, x_max):
        for s in sensors:
            if is_within_sensor((x,y), s) and (x,y) not in beacons:
                #print(x)
                ret += 1
                break
    return ret

# with open("input.txt", "r") as f:
#     data = f.read().split("\n")[:-1]

#     sensors = []
#     for line in data:
#         sensors.append(parse_sensor(line))
#     beacons = set([s.closest_beacon for s in sensors])
#     y=2000000
#     ret = process_ranges(-10000000,10000000,y,sensors,beacons)
#     print(ret)

def find_furthest_x_on_same_row(point, sensor):
    y_dist = abs(point[1] - sensor.position[1])
    remaining_dist = sensor.min_distance - y_dist
    return sensor.position[0]+remaining_dist


with open("input.txt", "r") as f:
    data = f.read().split("\n")[:-1]

    sensors = []
    for line in data:
        sensors.append(parse_sensor(line))
    beacons = set([s.closest_beacon for s in sensors])
    import pprint
    pprint.pprint(sensors)
    skip = False
    print([is_within_sensor((3999999,318154),s) for s in sensors])
    print((3999999,318154) in beacons)
    for y in range(4000001):
        x = 0
        while x < 4000001:
            furthest = max([find_furthest_x_on_same_row((x,y),s) for s in sensors if is_within_sensor((x,y),s)])
            #print(furthest)
            for i,s in enumerate(sensors):
                if is_within_sensor((furthest+1,y), s) or (x,y) in beacons:
                    break
                if i+1 == len(sensors) and (furthest+1) < 4000001:
                    print(furthest+1,y)
                    print(4000000*(furthest+1) + y)
                    exit()
            x = furthest + 1

