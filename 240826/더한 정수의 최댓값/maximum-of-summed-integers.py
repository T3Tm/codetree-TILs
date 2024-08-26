n = int(input())
arr = [0] + [*map(int,input().split())]
prefix = [0] * (n+1)

for i in range(1,n+1):
    prefix[i] = prefix[i-1] + arr[i]
result = 0

for i in range(2,n):
    now = (prefix[i-1] - prefix[1])
    now += (prefix[n] - prefix[i])*2
    result= max(result, now)

for i in range(n-1, 1,-1):
    now = prefix[i-1]*2
    now += prefix[n-1] - prefix[i]
    result = max(result, now)
print(result)