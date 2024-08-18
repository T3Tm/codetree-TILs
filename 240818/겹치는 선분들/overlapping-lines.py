import sys
input = sys.stdin.readline

n,k = map(int,input().split())

dic = {}

lis = set()
cur = 0
for i in range(n):
    s, e = input().split()
    s = int(s)
    if e == 'R':#오른쪽
        dic[cur] = dic.get(cur, 0) + 1
        dic[cur + s + 1] = dic.get(cur + s + 1, 0) - 1
        lis.add(cur + s + 1)
        lis.add(cur)
        cur+=s
    else:#왼쪽
        dic[cur - s] = dic.get(cur - s, 0) + 1
        dic[cur + 1] = dic.get(cur + 1, 0) - 1
        lis.add(cur - s)
        lis.add(cur + 1)
        cur-=s
    
lis = sorted(lis)
result = 0
for i in range(1,len(lis)):
    s = lis[i-1]
    e = lis[i]
    dic[e] += dic[s]
    if dic[s] >= k:#s부터는 k개가 겹침
        if dic[e] >= k:
            result += e - s
        else:#이전까지는 됨.
            result += (e-1) - s
print(result)