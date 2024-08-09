n = int(input())
hol = 0
jjak = 0
for i in map(int,input().split()):
    if i&1:hol += 1
    else: jjak += 1

result = t = min(jjak, hol)
jjak -= t
hol -= t

cnt = 0
if not hol:
    cnt = 1
else:#짝수가 다 썼음 2,1,2,1
    # 1일 때 2라면
    result += hol // 3
    hol %= 3
    if hol == 1:cnt = -2
    elif hol == 2:cnt = 1
print(result * 2 + cnt)