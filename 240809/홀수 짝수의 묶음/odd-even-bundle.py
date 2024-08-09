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
    minus = 2
    while hol:
        hol -= minus
        minus =2 if minus == 1 else 1
        cnt += 1
        if hol == 0:break
        elif hol < 0:
            cnt -= 2
            break
print(result * 2 + cnt)