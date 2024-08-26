n = int(input())
arr = [*map(int,input().split())]

result = 0

for i in range(1,n-1):
    now = sum(arr[1:i]+[0])
    now += sum(arr[i+1:]+[0])*2
    result = max(result, now)

for i in range(2,n):
    now = sum(arr[0:-i] + [0])*2
    now += sum(arr[-i + 1:-1] + [0])
    result = max(result, now)
print(result)