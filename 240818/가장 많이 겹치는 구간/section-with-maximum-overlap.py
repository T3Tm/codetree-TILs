import sys
input = sys.stdin.readline

# n,k = map(int,input().split())
n = int(input())
li = [[*map(int,input().split())]for _ in range(n)]

li.sort()

dic = {}

lis = set()
for s,e in li:
    dic[s] = dic.get(s, 0) + 1
    lis.add(s)
    dic[e] = dic.get(e, 0) - 1
    lis.add(e)


lis = sorted(lis)
result = 0
for i in range(1,len(lis)):
    s = lis[i-1]
    e = lis[i]
    dic[e] += dic[s]
    result = max(result, max(dic[e], dic[s]))
    # if dic[s] == k:#s부터는 k개가 겹침
    #     if dic[e] > k:
    #         result += e - s
    # else:#s부터 몇 개인지 모르겠지만 겹치게 됐음
    #     #s에서는 k개가 안되지만 e-1부터 e까지는 k개 된다는 것
    #     if dic[e] == k:#이러면 e-1일 때 k가 된다는 것
    #         result += 1
print(result)