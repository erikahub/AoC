"""
FROM: https://adventofcode.com/2019/day/4
--- Part Two ---
An Elf just remembered one more important detail: the two adjacent matching digits are not part of a larger group of matching digits.

Given this additional criterion, but still ignoring the range rule, the following are now true:

112233 meets these criteria because the digits never decrease and all repeated digits are exactly two digits long.
123444 no longer meets the criteria (the repeated 44 is part of a larger group of 444).
111122 meets the criteria (even though 1 is repeated more than twice, it still contains a double 22).
How many different passwords within the range given in your puzzle input meet all of the criteria?

Your puzzle input is still 197487-673251.
"""

keylength = 6
lower, upper = 197487, 673251
possibilities = 0

for n in range(lower, upper+1):
    n = str(n)
    ok = False
    for c in range(keylength-1):
        #if values decrease end with false
        if n[c] > n[c+1]:
            ok = False
            break
        if n[c] == n[c+1]:
            if ok == False:
                ok = True 
                if c > 1 and n[c] != n[c-1]:
                    ok = False
            elif ok == True and n[c] == n[c-1]:
                 ok = False
    if ok == True:
        possibilities+=1
        
print(possibilities)