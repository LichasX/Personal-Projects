# https://codebreaker.xyz/problem/lunchbox, tle by 0.51s from 0.5s
inputs = str(input()).split() #(n, m)
remaining_val = int(inputs[0])
count = 0
lst = [int(input()) for m in range(int(inputs[1]))]
x = min(lst)
while remaining_val > 0 and len(lst) > 0 and not(x > remaining_val):
  x = min(lst)
  remaining_val -= x
  lst.remove(x)
  count += 1
print(count)
