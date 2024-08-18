import sys 
input = sys.stdin.readline


n = int(input())
li = [[*map(int,input().split())]for _ in range(n)]

li.sort()

dic = {}

lis = set()
for (s,e) in li:
    dic[s] = dic.get(s, 0) + 1
    dic[e] = dic.get(e, 0) - 1
    lis.add(s)
    lis.add(e)

lis = sorted(lis)

first = lis[0]
result = 0
for idx in range(1, len(lis)):
    s,e = lis[idx-1],lis[idx]
    
    dic[e] += dic[s]
    if not dic[e]:
        result += e - first
    
    if not dic[s]:
        first = e
print(result)