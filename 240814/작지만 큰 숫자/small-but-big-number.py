from sortedcontainers import SortedSet

n, m =map(int,input().split())

dic = SortedSet(map(int,input().split()),key=lambda x: -x)

for num in map(int,input().split()):
    value = dic.bisect_left(num)
    if value == len(dic):
        print(-1)
    else:
        print(dic.pop(index=value))