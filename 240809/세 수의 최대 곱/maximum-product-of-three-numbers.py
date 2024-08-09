n = int(input())
li = [*map(int,input().split())]

minus = []
plus = []
for num in li:
    if num < 0:
        minus.append(num)
    else:
        plus.append(num)
#음수 2개, 양수 1개
#양수 3개
minus.sort()
plus.sort()

result = -1 * 10 ** 8
if len(plus) < 1:#음수가 정답일 때가 있을까
    result = minus[0] * minus[1] * minus[2]
elif len(plus) == 1:
    result = minus[0] * minus[1] * plus[-1]
elif n == 3 and len(plus) == 2:
    result = minus[0] * plus[0] * plus[1]
else:
    result = minus[0] * minus[1] * plus[-1]
    if len(plus) > 2:
        result = max(result, plus[-1] * plus[-2] * plus[-3])
print(result)