n,s = map(int,input().split())
lis = [*map(int,input().split())]
total = sum(lis)
r = 10**8
for i in range(n):
    for j in range(i+1,n):
        r = min(r,abs(s - (total - lis[i] - lis[j])))
print(r)