from heapq import*
n = int(input())

d = []

for i in map(int,input().split()):
    heappush(d,i)
    if len(d) < 3:
        print(-1)
    else:
        a = heappop(d)
        b = heappop(d)
        c = heappop(d)
        print(a * b * c)
        heappush(d,a)
        heappush(d,b)
        heappush(d,c)