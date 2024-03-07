# https://codebreaker.xyz/problem/lunchbox
inputs = str(input("")).split() #(n, m)
lst = []
remaining_val = int(inputs[0])
count = 0
for m in range(int(inputs[1])):
    k = int(input(""))
    lst.append(int(k))
while remaining_val > 0 and len(lst) > 0 and not(min(lst) > remaining_val):
    remaining_val -= min(lst)
    lst.remove(min(lst))
    count += 1
print(count)
