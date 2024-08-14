n = int(input())

dic = {}
for _ in range(n):
    word = input()
    dic[word] = dic.get(word,0) + 1

for word in sorted(dic.keys()):
    print(word, dic[word])