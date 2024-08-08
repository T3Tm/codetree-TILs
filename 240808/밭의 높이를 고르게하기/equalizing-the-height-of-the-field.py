n,h,t=map(int,input().split())
li = [*map(int,input().split())]
#연속하여 H 높이어야 한다.
result = 10**8


for i in range(n):
    now = 0
    for j in range(i,i+t):
        if j == n:
            now = 10 ** 8
            break
        now += abs(li[j] - h)
    result = min(result,now)
print(result)