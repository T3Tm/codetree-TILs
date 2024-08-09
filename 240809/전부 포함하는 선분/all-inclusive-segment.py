n = int(input())
li = [[*map(int,input().split())]for _ in range(n)]
lis = li[::]
li.sort(key = lambda x: (x[0], -x[1]))

lis.sort(key = lambda x: (-x[1], x[0]))

#최소, 최대를 지정하기.
mini = li[1][0]
maxi = 0
for i in range(1,n):
    maxi = max(maxi, li[i][1])

result = maxi - mini

maxi = lis[1][1]
mini = 101
for i in range(1,n):
    mini = min(mini, lis[i][0])
result = min(result, maxi - mini)

print(result)