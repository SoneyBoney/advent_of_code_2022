from enum import IntEnum
import copy


class Resource(IntEnum):
    ORE = 0
    CLAY = 1
    OBSIDIAN = 2
    GEODE = 3


class Blueprint:
    def __init__(self, line: str):
        self.n = None
        self.bots = []
        self.parse_blueprint(line)

    def parse_blueprint(self, line: str):
        self.n = int(line.split(":")[0].split(" ")[-1])
        temp = line.split(":")[1].split(". ")
        self.bots.append((int(temp[0].split(" ")[5]), 0, 0))
        self.bots.append((int(temp[1].split(" ")[4]), 0, 0))
        self.bots.append((int(temp[2].split(" ")[4]), int(temp[2].split(" ")[7]), 0))
        self.bots.append((int(temp[3].split(" ")[4]), 0, int(temp[3].split(" ")[7])))

    def __repr__(self):
        return f"<Blueprint #{self.n}: ore_bot: {self.ore_bot}, clay_bot: {self.clay_bot}, obsidian_bot {self.obsidian_bot}, geode_bot: {self.geode_bot}"



def max_geodes(
    time: int,
    blueprint: Blueprint,
    ore: int,
    ore_robots: int,
    clay: int,
    clay_robots: int,
    obsidian: int,
    obsidian_robots: int,
    geode: int,
    geode_robots: int,
    memoize,
) -> int:
    if time <= 0:
        return geode
    
    # since greedy is optimal, we never need more robots to build more than 1 unit of each robot
    # solutions that include misallocated resources are pruned and exit early if already seen
    max_ore_cost = max([x[0] for x in blueprint.bots])
    if ore_robots >= max_ore_cost:
        ore_robots = max_ore_cost
    max_clay_cost = max([x[1] for x in blueprint.bots])
    if clay_robots >= max_clay_cost:
        clay_robots = max_clay_cost
    max_obsidian_cost = max([x[2] for x in blueprint.bots])
    if obsidian_robots >= max_obsidian_cost:
        obsidian_robots = max_obsidian_cost
    if ore >= time*max_ore_cost - ore_robots*(time-1):
        ore = time*max_ore_cost - ore_robots*(time-1)
    if clay >= time*max_clay_cost - clay_robots*(time-1):
        clay = time*max_clay_cost - clay_robots*(time-1)
    if obsidian >= time*max_obsidian_cost - obsidian_robots*(time-1):
        obsidian = time*max_obsidian_cost - obsidian_robots*(time-1)

    key = (time,ore,ore_robots,clay,clay_robots,obsidian,obsidian_robots,geode,geode_robots)
    if key in memoize.keys():
        return memoize[key]
    ret = 0
    ret = max(ret,max_geodes(time-1,blueprint,ore+ore_robots,ore_robots,clay+clay_robots,clay_robots,obsidian+obsidian_robots,obsidian_robots,geode+geode_robots,geode_robots,memoize))
    if ore >= blueprint.bots[Resource.ORE][Resource.ORE]:
        ret = max(ret,max_geodes(time-1,blueprint,ore+ore_robots-blueprint.bots[Resource.ORE][Resource.ORE],ore_robots+1,clay+clay_robots,clay_robots,obsidian+obsidian_robots,obsidian_robots,geode+geode_robots,geode_robots,memoize))
    if ore >= blueprint.bots[Resource.CLAY][Resource.ORE]:
        ret = max(ret,max_geodes(time-1,blueprint,ore+ore_robots-blueprint.bots[Resource.CLAY][Resource.ORE],ore_robots,clay+clay_robots,clay_robots+1,obsidian+obsidian_robots,obsidian_robots,geode+geode_robots,geode_robots,memoize))
    if ore >= blueprint.bots[Resource.OBSIDIAN][Resource.ORE] and clay >= blueprint.bots[Resource.OBSIDIAN][Resource.CLAY]:
        ret = max(ret,max_geodes(time-1,blueprint,ore+ore_robots-blueprint.bots[Resource.OBSIDIAN][Resource.ORE],ore_robots,clay+clay_robots-blueprint.bots[Resource.OBSIDIAN][Resource.CLAY],clay_robots,obsidian+obsidian_robots,obsidian_robots+1,geode+geode_robots,geode_robots,memoize))
    if ore >= blueprint.bots[Resource.GEODE][Resource.ORE] and obsidian >= blueprint.bots[Resource.GEODE][Resource.OBSIDIAN]:
        ret = max(ret,max_geodes(time-1,blueprint,ore+ore_robots-blueprint.bots[Resource.GEODE][Resource.ORE],ore_robots,clay+clay_robots,clay_robots,obsidian+obsidian_robots-blueprint.bots[Resource.GEODE][Resource.OBSIDIAN],obsidian_robots,geode+geode_robots,geode_robots+1,memoize))

    memoize[key] = ret
    return ret


# with open("input.txt", "r") as f:
#     data = f.read().split("\n")[:-1]

#     blueprints = []
#     for line in data:
#         blueprints.append(Blueprint(line))
#     ret = 0
#     for b in blueprints:
#         temp= max_geodes(24, b, 0, 1, 0, 0, 0, 0, 0, 0,{}) * b.n
#         print(temp)
#         ret += temp
#     print(ret)
with open("input.txt", "r") as f:
    data = f.read().split("\n")[:-1]

    blueprints = []
    for line in data:
        blueprints.append(Blueprint(line))
    ret = 1
    for b in blueprints[:3]:
        temp= max_geodes(32, b, 0, 1, 0, 0, 0, 0, 0, 0,{})
        print(temp)
        ret *= temp
    print(ret)
