n = int(input())

dic = {}
for _ in range(n):
    word = input()
    dic[word] = dic.get(word, 0) + 1

print(max(dic.values()))