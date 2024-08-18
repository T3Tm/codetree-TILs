import sys
input = sys.stdin.readline

n = int(input())

li = [[*map(int,input().split())] for _ in range(n)]

li.sort()

dic = {}
lis = set()
for (h, x, y) in li:#h가 더 낮은 것부터 처리를 시작하는데
    dic[x] = dic.get(x, 0) + 1
    dic[y] = dic.get(y, 0) - 1
    lis.add(x)
    lis.add(y)
lis = sorted(lis)
cnt = 0 
for idx in range(1, len(lis)):
    s,e = lis[idx-1], lis[idx]
    #해당 구간까지 더 낮은 아이가 처리 해주기
    dic[e] += dic[s]
    if dic[s] == 1 or dic[e] == 1:
        cnt += 1
print(cnt)