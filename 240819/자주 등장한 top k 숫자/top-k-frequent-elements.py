n, k =map(int,input().split())

dic = {}
for i in map(int,input().split()):
    dic[i] = dic.get(i, 0) + 1

filter_sort = sorted(dic.items(), key = lambda x: (-x[1], -x[0]))
print(*[*map(lambda x: x[0], filter_sort)][:k])