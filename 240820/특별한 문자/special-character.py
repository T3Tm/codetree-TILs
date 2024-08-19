word = input()

dic = {}

for i in word:
    dic[i] = dic.get(i, 0) + 1


filter_list = [*filter(lambda x: x[1] == 1, dic.items())] + [(None, None)]

print(filter_list[0][0])