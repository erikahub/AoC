
origin = (0,0)
wireA = list()
wireB = list()

#expected results for testcase 1 is 159, for testcase 2 it is 135
# wireA, wireB = open('Day3/testpaths1.txt').read().split('\n')
# wireA, wireB = open('Day3/testpaths2.txt').read().split('\n')
wireA, wireB = open('Day3/wirepaths.txt').read().split('\n')
wireA, wireB = [x.split(',') for x in [wireA, wireB]]

pathA = [*((a[0], a[1:]) for a in wireA)]
pathB = [*((b[0], b[1:]) for b in wireB)]
#horizontal
h = ['R', 'L']
#vertical
v = ['U', 'D']
currentA = origin
currentB = origin
for a in pathA:
    dirA = a[0]
    stepA = a[1]
    for b in pathB:
        dirB = b[0]
        stepB = b[1]
        # assert dirA, dirB in ['R', 'L', 'D', 'U']
        if dirA in h:
            if dirB in h:
                if currentA[1] == currentB[1]:
                    if abs(stepA)-abs(currentA[0]) <= abs(stepB) - abs(currentB):
                        

    if dirA == 'R':
        currentA[0]+=stepA
    elif dirA == 'L':
        currentA[0]+=stepA
    elif dirA == 'D':
        currentA[1]+=stepA
    elif dirA == 'U':
        currentA[1]+=stepA