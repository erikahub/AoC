def calculate(split: list): 
    i=0
    while split[i] != 99:
        #i < len(split) and 
        if split[i] == 1:
            # print('pos(%i) = pos(%i) + pos(%i)' % (split[i+3], split[i+1], split[i+2]))
            # print('%i = %i + %i' % ( split[split[i+1]]+split[split[i+2]],  split[split[i+1]], split[split[i+2]]))
            split[split[i+3]] = split[split[i+1]]+split[split[i+2]]
        elif split[i] == 2:
        	split[split[i+3]] = split[split[i+1]]*split[split[i+2]]
        else:
            print('unknown operation')
        i+=4
    return split
	# print(split[0])


#test cases
expectedResult = [3500,9,10,70,2,3,11,0,99,30,40,50]
line = [1,9,10,3,2,3,11,0,99,30,40,50]
print('Test 1:', calculate(line) == expectedResult)
expectedResult = [2,0,0,0,99]
line = [1,0,0,0,99]
print('Test 2:', calculate(line) == expectedResult)
expectedResult = [2,3,0,6,99]
line = [2,3,0,3,99]
print('Test 3:', calculate(line) == expectedResult)
expectedResult = [2,4,4,5,99,9801]
line = [2,4,4,5,99,0]
print('Test 4:', calculate(line) == expectedResult)
expectedResult = [30,1,1,4,2,5,6,0,99]
line = [1,1,1,4,99,5,6,0,99]
print('Test 5:', calculate(line) == expectedResult)

split = list()
# split = [ int(i) for i in line.split(',') ]

#read from file
with open('Day2/input.txt') as file:
    split = [ int(i) for i in file.readlines(1)[0].split(',') ]
    
split[1] = 12
split[2] = 2
print("Result:", calculate(split)[0])