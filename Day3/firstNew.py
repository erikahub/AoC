
origin = (0,0)
wireA = list()
wireB = list()

#expected results for testcase 1 is 159, for testcase 2 it is 135
# wireA, wireB = open('Day3/testpaths1.txt').read().split('\n')
# wireA, wireB = open('Day3/testpaths2.txt').read().split('\n')
wireA, wireB = open('Day3/wirepaths.txt').read().split('\n')
wireA, wireB = [x.split(',') for x in [wireA, wireB]]

