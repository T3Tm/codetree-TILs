n, k =map(int,input().split())

dic = {}
for i in map(int,input().split()):
    dic[i] = dic.get(i, 0) + 1


print(*map(lambda x: x[0],sorted(filter(lambda x: x[1]>=k, dic.items()), key = lambda x: (x[1], -x[0]))))