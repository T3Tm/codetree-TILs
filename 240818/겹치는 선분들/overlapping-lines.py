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
        dic[cur + s] = dic.get(cur + s, 0) - 1
        lis.add(cur + s)
        lis.add(cur)
        cur+=s
    else:#왼쪽
        dic[cur - s] = dic.get(cur - s, 0) + 1
        dic[cur] = dic.get(cur, 0) - 1
        lis.add(cur - s)
        lis.add(cur)
        cur-=s
lis = sorted(lis)
result = 0
for i in range(1,len(lis)):
    s = lis[i-1]
    e = lis[i]
    dic[e] += dic[s]
    if dic[s] >= k:#s부터는 k개가 겹침
        result += e - s
print(result)