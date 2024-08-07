n,t = map(int,input().split())
lis = [*map(int,input().split())]

idx=0
result = s = 0
while idx < n:
    while idx < n and lis[idx] <= t:idx+=1
    if idx == n :break
    left = idx
    while left < n and lis[left] > t:left+=1
    result = max(result,left - idx)
    idx = left
print(result)