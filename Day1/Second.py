allModules = list()

with open("Day1/fuel.txt", 'r') as file:
    for line in file:
        allModules.append(int(line))
    

# print(allModules)

result = 0
# value = 100756
for value in allModules:
    value = value//3-2
    while value >= 0:
        # print(value)
        result += value
        value = value//3-2

print(result)
