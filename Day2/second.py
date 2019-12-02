"""
list of intcodes are used as initial state of memory[...]

For example, in the instruction 1,2,3,4, 1 is the opcode; 2, 3, and 4 are the parameters

The address of the current instruction is called the instruction pointer; it starts at 0. 
After an instruction finishes, the instruction pointer increases by the number 
of values in the instruction;

!!! you need to determine what pair of inputs produces the output 19690720

"""

def findPair(split: list):
    for x in range(100):
        for y in range(100):
            split[1]=x
            split[2]=y
            i=0
            while split[i] != 99:
                opcode = split[i]
                #i < len(split) and 
                if opcode == 1:
                    print('pos(%i) = pos(%i) + pos(%i) with i = %i' % (split[i+3], split[i+1], split[i+2], i))
                    print('%i = %i + %i' % ( split[split[i+1]]+split[split[i+2]],  split[split[i+1]], split[split[i+2]]))
                    split[split[i+3]] = split[split[i+1]] + split[split[i+2]]
                elif opcode == 2:
                    split[split[i+3]] = split[split[i+1]] * split[split[i+2]]
                else:
                    print('unknown operation')
                i+=4
            if split[0] == 19690720:
                print(x, y)
    # return list()
        	# print(split[0])


split = list()
# split = [ int(i) for i in line.split(',') ]

#read from file
with open('Day2/input.txt') as file:
    split = [ int(x) for x in file.readlines(1)[0].split(',') ]
    
print(split[56:58])
# print(findPair(split))