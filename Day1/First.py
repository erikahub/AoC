allModules = list()

# tests = [ 12, 14, 1969, 100756]
# results = [2, 2, 654, 33583]

with open("Day1/fuel.txt", 'r') as file:
    for line in file:
        allModules.append(int(line))
    
# print(allModules)
# print(len(allModules))

result = 0
for value in allModules:
    result+=((value//3)-2)

print(result)
