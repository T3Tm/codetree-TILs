a, b = map(int,input().split())


modb = [0] * b
while a:
    modb[a % b]+=1
    a//=b

total = 0
for i in range(b):
    total += modb[i] ** 2
print(total)