"""
FROM: https://adventofcode.com/2019/day/7
--- Day 7: Amplification Circuit ---
Based on the navigational maps, you're going to need to send more power to your ship's thrusters to reach Santa in time. To do this, you'll need to configure a series of amplifiers already installed on the ship.

There are five amplifiers connected in series; each one receives an input signal and produces an output signal. They are connected such that the first amplifier's output leads to the second amplifier's input, the second amplifier's output leads to the third amplifier's input, and so on. The first amplifier's input value is 0, and the last amplifier's output leads to your ship's thrusters.

    O-------O  O-------O  O-------O  O-------O  O-------O
0 ->| Amp A |->| Amp B |->| Amp C |->| Amp D |->| Amp E |-> (to thrusters)
    O-------O  O-------O  O-------O  O-------O  O-------O
The Elves have sent you some Amplifier Controller Software (your puzzle input), a program that should run on your existing Intcode computer. Each amplifier will need to run a copy of the program.

When a copy of the program starts running on an amplifier, it will first use an input instruction to ask the amplifier for its current phase setting (an integer from 0 to 4). Each phase setting is used exactly once, but the Elves can't remember which amplifier needs which phase setting.

The program will then call another input instruction to get the amplifier's input signal, compute the correct output signal, and supply it back to the amplifier with an output instruction. (If the amplifier has not yet received an input signal, it waits until one arrives.)

Your job is to find the largest output signal that can be sent to the thrusters by trying every possible combination of phase settings on the amplifiers. Make sure that memory is not shared or reused between copies of the program.

For example, suppose you want to try the phase setting sequence 3,1,2,4,0, which would mean setting amplifier A to phase setting 3, amplifier B to setting 1, C to 2, D to 4, and E to 0. Then, you could determine the output signal that gets sent from amplifier E to the thrusters with the following steps:

Start the copy of the amplifier controller software that will run on amplifier A. At its first input instruction, provide it the amplifier's phase setting, 3. At its second input instruction, provide it the input signal, 0. After some calculations, it will use an output instruction to indicate the amplifier's output signal.
Start the software for amplifier B. Provide it the phase setting (1) and then whatever output signal was produced from amplifier A. It will then produce a new output signal destined for amplifier C.
Start the software for amplifier C, provide the phase setting (2) and the value from amplifier B, then collect its output signal.
Run amplifier D's software, provide the phase setting (4) and input value, and collect its output signal.
Run amplifier E's software, provide the phase setting (0) and input value, and collect its output signal.
The final output signal from amplifier E would be sent to the thrusters. However, this phase setting sequence may not have been the best one; another sequence might have sent a higher signal to the thrusters.

Here are some example programs:

Max thruster signal 43210 (from phase setting sequence 4,3,2,1,0):

3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0
Max thruster signal 54321 (from phase setting sequence 0,1,2,3,4):

3,23,3,24,1002,24,10,24,1002,23,-1,23,
101,5,23,23,1,24,23,23,4,23,99,0,0
Max thruster signal 65210 (from phase setting sequence 1,0,4,3,2):

3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,
1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0
Try every combination of phase settings on the amplifiers. What is the highest signal that can be sent to the thrusters?
"""

from itertools import permutations

phases = 4
phaseSetting = [_ for _ in permutations(range(phases+1), phases+1)]
ampOutput = 0
POSITIONMODE = 0
IMMEDIATEMODE = 1

input_ = 0

def calculate(sequence: list, input_: int):
    i=0
    ret = 0

    ops = list()
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
        ops.append(OPCode)
        p1, p2, p3 = i+1, i+2, i+3
        if OPCode == 1:
            sequence[sequence[p3]] = sequence[_getIndex_(modes[2],p1)]+sequence[_getIndex_(modes[1],p2)]
            i+=4
        elif OPCode == 2:
            sequence[sequence[p3]] = sequence[_getIndex_(modes[2],p1)]*sequence[_getIndex_(modes[1],p2)]
            i+=4
        elif OPCode == 3:
            sequence[sequence[p1]] = input_
            input_ = ampOutput
            i+=2 
        elif OPCode == 4:
            #CHANGED FROM PRINT TO RETURN
            ret = sequence[_getIndex_(modes[2], p1)]
            i+=2
        elif OPCode == 5:
            i = sequence[_getIndex_(modes[1], p2)] if sequence[_getIndex_(modes[2], p1)] != 0 else i+3
        elif OPCode == 6:
            i = sequence[_getIndex_(modes[1], p2)] if sequence[_getIndex_(modes[2], p1)] == 0 else i+3
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

    return ret

split = list()
#test1, expected 43210
split = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]

#read from file
# with open('Day7/input.txt') as file:
    # split = [ int(i) for i in file.readlines(1)[0].split(',') ]

thrusterSignals = list()
#for possible phase combinations
for c in phaseSetting:
    #for phases in combination
    for val in c:
        input_ = val
        ampOutput = calculate(split, input_)
        thrusterSignals.append(ampOutput)


print(max(thrusterSignals))