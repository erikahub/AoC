"""
FROM: https://adventofcode.com/2019/day/3
--- Day 3: Crossed Wires ---
The gravity assist was successful, and you're well on your way to the Venus refuelling station. During the rush back on Earth, the fuel management system wasn't completely installed, so that's next on the priority list.

Opening the front panel reveals a jumble of wires. Specifically, two wires are connected to a central port and extend outward on a wirePath. You trace the path each wire takes as it leaves the central port, one wire per line of text (your puzzle input).

The wires twist and turn, but the two wires occasionally cross paths. To fix the circuit, you need to find the intersection point closest to the central port. Because the wires are on a wirePath, use the Manhattan distance for this measurement. While the wires do technically cross right at the central port where they both start, this point does not count, nor does a wire count as crossing with itself.

For example, if the first wire's path is R8,U5,L5,D3, then starting from the central port (o), it goes right 8, up 5, left 5, and finally down 3:

...........
...........
...........
....+----+.
....|....|.
....|....|.
....|....|.
.........|.
.o-------+.
...........
Then, if the second wire's path is U7,R6,D4,L4, it goes up 7, right 6, down 4, and left 4:

...........
.+-----+...
.|.....|...
.|..+--X-+.
.|..|..|.|.
.|.-X--+.|.
.|..|....|.
.|.......|.
.o-------+.
...........
These wires cross at two locations (marked X), but the lower-left one is closer to the central port: its distance is 3 + 3 = 6.

Here are a few more examples:

R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83 = distance 159
R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7 = distance 135
What is the Manhattan distance from the central port to the closest intersection?
"""

origin = (0,0)
firstWire = list()
secondWire = list()

#expected results for testcase 1 is 159, for testcase 2 it is 135
# with open('Day3/testpaths1.txt') as file:
# with open('Day3/testpaths2.txt') as file:
with open('Day3/wirepaths.txt') as file:
    line = file.readlines()
    firstWire += (s.replace('\n', '') for s in line[0].split(','))
    secondWire += line[1].split(',')

"""idea! save operations in tuples and look for distances between previous and current"""
def getNodes(wire: list) -> list:
    #initialising paths with central port assuming x=0, y=0
    wirePath = [origin]
    for elem in wire:
        direction = elem[0]
        step = int(elem[1:])
        if direction == 'R':
            # wirePath.append(wirePath[-1])
            # wirePath[-1] = (direction, wirePath[-1][1] + step, wirePath[-1][2])
            wirePath += [*((wirePath[-1][0] + i, wirePath[-1][1])for i in range(1, step+1))]
        elif direction == 'L':
            # wirePath.append(wirePath[-1])
            # wirePath[-1] = (direction, wirePath[-1][1] - step, wirePath[-1][2])
            wirePath += [*((wirePath[-1][0] - i, wirePath[-1][1])for i in range(1, step+1))]
        elif direction == 'U':
            # wirePath.append(wirePath[-1])
            # wirePath[-1] = (direction, wirePath[-1][1], wirePath[-1][2] + step)
            wirePath += [*((wirePath[-1][0], wirePath[-1][1] + i)for i in range(1, step+1))]
        elif direction == 'D':
            # wirePath.append(wirePath[-1])
            # wirePath[-1] = (direction, wirePath[-1][1], wirePath[-1][2] - step)
            wirePath += [*((wirePath[-1][0], wirePath[-1][1] - i)for i in range(1, step+1))]
    return wirePath


intersections = list()
#get all coordinates where the wires run minus the startpoint
nodesFirst = getNodes(firstWire)[1:]
print("constructed first set of nodes")
nodesSecond = getNodes(secondWire)[1:]
print("constructed all nodes")
intersections += [*(pairFirst for pairFirst in nodesFirst if pairFirst in nodesSecond)]
print("intersections calculated")
# print(intersections)
#print smallest Manhattan Distance
print(min(*(abs(value[0])+abs(value[1]) for value in intersections)))
