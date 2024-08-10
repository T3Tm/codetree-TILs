n = int(input())

arr = [-1] * 11

cnt = 0
for i in range(n):
    num, road = map(int,input().split())
    if arr[num] != road:
        cnt += 1
    arr[num] = road
print(cnt - (11 - arr.count(-1)))