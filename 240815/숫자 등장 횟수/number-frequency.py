n, m = map(int,input().split())

dic = {}
for num in map(int,input().split()):
    dic[num] = dic.get(num, 0) + 1

for num in map(int,input().split()):
    print(dic.get(num,0), end=' ')