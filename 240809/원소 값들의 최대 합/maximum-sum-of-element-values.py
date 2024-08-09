n,m = map(int,input().split())
li = [0] + [*map(int,input().split())]
result = 0
for i in range(1,n+1):
    s = i
    now = 0
    for i in range(m):
        now += s
        s = li[s]
    result = max(result,now)
print(result)