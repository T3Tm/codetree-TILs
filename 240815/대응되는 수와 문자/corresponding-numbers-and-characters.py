n, m = map(int,input().split())

dic = {}

for idx in range(1, n+1):
    word = input()
    dic[word] = idx
    dic[f'{idx}'] = word

for _ in range(m):
    inp = input()
    print(dic[inp])