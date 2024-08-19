n = int(input())
a = [*map(int,input().split())]
b = [*map(int,input().split())]

ab = {}

for i in range(n):
    for j in range(n):
        ab[a[i] + b[j]] = ab.get(a[i]+b[j], 0) + 1


c = [*map(int,input().split())]
d = [*map(int,input().split())]

cnt = 0
for i in range(n):
    for j in range(n):
        v = c[i] + d[j]
        if -v in ab:
            cnt += ab[-v]
print(cnt)