n = int(input())

dic = {}
for _ in range(n):
    cmd, k ,*v = input().split()
    if cmd == 'add':
        dic[k] = v[0]
    elif cmd == 'remove':
        dic.pop(k)
    else:
        print(dic.get(k, None))