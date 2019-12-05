"""
FROM: https://adventofcode.com/2019/day/5
--- Part Two ---
The air conditioner comes online! Its cold air feels good for a while, but then the TEST alarms start to go off. Since the air conditioner can't vent its heat anywhere but back into the spacecraft, it's actually making the air inside the ship warmer.

Instead, you'll need to use the TEST to extend the thermal radiators. Fortunately, the diagnostic program (your puzzle input) is already equipped for this. Unfortunately, your Intcode computer is not.

Your computer is only missing a few opcodes:

Opcode 5 is jump-if-true: if the first parameter is non-zero, it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing.
Opcode 6 is jump-if-false: if the first parameter is zero, it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing.
Opcode 7 is less than: if the first parameter is less than the second parameter, it stores 1 in the position given by the third parameter. Otherwise, it stores 0.
Opcode 8 is equals: if the first parameter is equal to the second parameter, it stores 1 in the position given by the third parameter. Otherwise, it stores 0.
Like all instructions, these instructions need to support parameter modes as described above.

Normally, after an instruction is finished, the instruction pointer increases by the number of values in that instruction. However, if the instruction modifies the instruction pointer, that value is used and the instruction pointer is not automatically increased.

For example, here are several programs that take one input, compare it to the value 8, and then produce one output:

3,9,8,9,10,9,4,9,99,-1,8 - Using position mode, consider whether the input is equal to 8; output 1 (if it is) or 0 (if it is not).
3,9,7,9,10,9,4,9,99,-1,8 - Using position mode, consider whether the input is less than 8; output 1 (if it is) or 0 (if it is not).
3,3,1108,-1,8,3,4,3,99 - Using immediate mode, consider whether the input is equal to 8; output 1 (if it is) or 0 (if it is not).
3,3,1107,-1,8,3,4,3,99 - Using immediate mode, consider whether the input is less than 8; output 1 (if it is) or 0 (if it is not).
Here are some jump tests that take an input, then output 0 if the input was zero or 1 if the input was non-zero:

3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9 (using position mode)
3,3,1105,-1,9,1101,0,0,12,4,12,99,1 (using immediate mode)
Here's a larger example:

3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99
The above example program uses an input instruction to ask for a single number. The program will then output 999 if the input value is below 8, output 1000 if the input value is equal to 8, or output 1001 if the input value is greater than 8.

This time, when the TEST diagnostic program runs its input instruction to get the ID of the system to test, provide it 5, the ID for the ship's thermal radiator controller. This diagnostic test suite only outputs one number, the diagnostic code.

What is the diagnostic code for system ID 5?
"""

POSITIONMODE = 0
IMMEDIATEMODE = 1

# input_ = int(input("Input:"))
input_ = 8

def calculate(sequence: list): 
    i=0
    
    def _getIndex_(mode: int, index: int):
        if mode == POSITIONMODE:
            return sequence[index]
        elif mode == IMMEDIATEMODE:
            return index
        return None

    init = [int(i) for i in str(sequence[i])]
    # modes = [A, B, C, D, E]
    #A - mode of 3rd parameter, B - mode of 2nd parameter, C - mode of 1st parameter, DE - two-digit opcode
    modes = [POSITIONMODE,POSITIONMODE,POSITIONMODE,POSITIONMODE,POSITIONMODE]
    for s in range(0, len(init)):
        modes[len(modes)-s-1] = init[-s-1]
    OPCode = modes[-2]*10 + modes[-1]
    while OPCode != 99:
        p1, p2, p3 = i+1, i+2, i+3
        if OPCode == 1:
            sequence[sequence[p3]] = sequence[_getIndex_(modes[2],p1)]+sequence[_getIndex_(modes[1],p2)]
            i+=4
        elif OPCode == 2:
            sequence[sequence[p3]] = sequence[_getIndex_(modes[2],p1)]*sequence[_getIndex_(modes[1],p2)]
            i+=4
        elif OPCode == 3:
            sequence[sequence[p1]] = input_
            i+=2
        elif OPCode == 4:
            print(sequence[_getIndex_(modes[2], p1)])
            i+=2
        elif OPCode == 5:
            if sequence[_getIndex_(modes[2], p1)] != 0:
                i = sequence[_getIndex_(modes[1], p2)]
        elif OPCode == 6:
            if sequence[_getIndex_(modes[2], p1)] == 0:
                i = sequence[_getIndex_(modes[1], p2)]
        elif OPCode == 7:
            sequence[sequence[p3]] = 1 if sequence[_getIndex_(modes[2], p1)] < sequence[_getIndex_(modes[1], p2)] else 0 
            i+=4
        elif OPCode == 8:
            sequence[sequence[p3]] = 1 if sequence[_getIndex_(modes[2], p1)] == sequence[_getIndex_(modes[1], p2)] else 0 
            i+=4
        else:
            print('unknown operation')
            i+=4
        
        init = [int(i) for i in str(sequence[i])]
        modes = modes = [POSITIONMODE,POSITIONMODE,POSITIONMODE,POSITIONMODE,POSITIONMODE]
        for s in range(0, len(init)):
            modes[len(modes)-s-1] = init[-s-1]
        OPCode = modes[-2]*10 + modes[-1]

    return sequence


def test():
    global input_
    line = [3,9,8,9,10,9,4,9,99,-1,8]
    input_ = 8
    print('Test 1: 1 =', end=' ')
    calculate(line)
    input_ = 2
    print('Test 2: 0 =', end=' ')
    calculate(line)
    input_ = 123
    print('Test 3: 0 =', end=' ')
    calculate(line)
    
    line = [3,9,7,9,10,9,4,9,99,-1,8]  
    input_ = 8
    print('Test 4: 0 =', end=' ')
    calculate(line)
    input_ = 2
    print('Test 5: 1 =', end=' ')
    calculate(line)
    input_ = 123
    print('Test 6: 0 =', end=' ')
    calculate(line)

    line = [3,3,1108,-1,8,3,4,3,99]  
    input_ = 8
    print('Test 7: 1 =', end=' ')
    calculate(line)
    input_ = 2
    print('Test 8: 0 =', end=' ')
    calculate(line)
    input_ = 123
    print('Test 9: 0 =', end=' ')
    calculate(line)

    line = [3,3,1107,-1,8,3,4,3,99]  
    input_ = 8
    print('Test 10: 0 =', end=' ')
    calculate(line)
    input_ = 2
    print('Test 11: 1 =', end=' ')
    calculate(line)
    input_ = 123
    print('Test 12: 0 =', end=' ')
    calculate(line)
    
    line = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]  
    input_ = 0
    print('Test 13: 0 =', end=' ')
    calculate(line)
    input_ = -12
    print('Test 14: 1 =', end=' ')
    calculate(line)
    input_ = 123
    print('Test 15: 1 =', end=' ')
    calculate(line)
    
    line = [3,3,1105,-1,9,1101,0,0,12,4,12,99,1]  
    input_ = 0
    print('Test 16: 0 =', end=' ')
    calculate(line)
    input_ = -12
    print('Test 17: 1 =', end=' ')
    calculate(line)
    input_ = 123
    print('Test 18: 1 =', end=' ')
    calculate(line)
    
    line = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
        1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
        999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]  
    input_ = 8
    print('Test 19: 1000 =', end=' ')
    calculate(line)
    input_ = 2
    print('Test 20: 999 =', end=' ')
    calculate(line)
    input_ = 123
    print('Test 21: 1001 =', end=' ')
    calculate(line)

test()

# split = list()
#read from file
# with open('Day5/input.txt') as file:
    # split = [ int(i) for i in file.readlines(1)[0].split(',') ]
    
# calculate(split)
