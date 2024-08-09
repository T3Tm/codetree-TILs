n,m = map(int,input().split())
num = list(map(int,input().split()))
dic ={}
for i in num:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i]+=1 
for _ in range(m):
    s = int(input())
    print(dic.get(s,0))