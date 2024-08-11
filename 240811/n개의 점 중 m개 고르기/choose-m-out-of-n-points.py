from itertools import combinations
n, m = map(int,input().split())
li = [[*map(int,input().split())] for _ in range(n)]

result = 10 ** 8
for comb in combinations(li,m):
    now = 0
    for co in combinations(comb,2):
        x1,x2 = co[0]
        x3,x4 = co[1]
        now = max(now,(x3 - x1)**2 + (x4-x2)**2)
    result= min(result, now)
print(result)