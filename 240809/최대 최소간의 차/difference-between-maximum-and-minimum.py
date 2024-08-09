n,k = map(int,input().split())
li = [*map(int,input().split())]
result = 10 ** 8
for i in range(n):
    #최소 일때
    now = 0
    for j in range(n):
        if li[i] <= li[j] <= li[i] + k:continue
        now += min(abs( li[j] - li[i]),abs( li[i]+k - li[j]))
    result = min(result,now)
    now = 0
    #최대 일때
    for j in range(n):
        if li[i]-k <= li[j] <= li[i]:continue
        now += min(abs(li[i] - li[j]), abs(li[j] - (li[i]-k)))
    result = min(result,now)
print(result)