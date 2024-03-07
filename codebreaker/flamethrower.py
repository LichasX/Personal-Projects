# https://codebreaker.xyz/problem/flamethrower

inputs = str(input("")).split()
trees = input("").split()
total = 0
output = 0
for tree in range(int(inputs[0])):
    total += int(trees[tree])
    for iteration in range(1, int(inputs[1])):
        if tree + iteration < len(trees):
            total += int(trees[tree + iteration])
    output = max(total, output)
    total = 0
print(output)
