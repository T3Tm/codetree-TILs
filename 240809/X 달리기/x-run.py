from math import ceil
x = int(input())

result = 0

minus = 1
while x - (minus << 1) > 0:
    x -= minus << 1
    result += 2
    minus += 1
result += ceil(x / minus)
print(result)