"""
FROM: https://adventofcode.com/2019/day/4
--- Day 4: Secure Container ---
You arrive at the Venus fuel depot only to discover it's protected by a password. The Elves had written the password on a sticky note, but someone threw it out.

However, they do remember a few key facts about the password:

It is a six-digit number.
The value is within the range given in your puzzle input.
Two adjacent digits are the same (like 22 in 122345).
Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
Other than the range rule, the following are true:

111111 meets these criteria (double 11, never decreases).
223450 does not meet these criteria (decreasing pair of digits 50).
123789 does not meet these criteria (no double).
How many different passwords within the range given in your puzzle input meet these criteria?

Your puzzle input is 197487-673251.
"""

keylength = 6
lower, upper = 197487, 673251
possibilities = 0

for n in range(lower, upper+1):
    n = str(n)
    ok = False
    for c in range(keylength-1):
        if ok == False and n[c] == n[c+1]:
            ok = True    
        if n[c] > n[c+1]:
            ok = False
            break
    if ok == True:
        possibilities+=1
        # print(n)
    
print(possibilities)
# print('10'[0] < '11'[0])
# if re.search('[(11)|(22)|(33)|(44)|(55)|(66)|(77)|(88)|(99)]', '101010'):
	# print('yes')