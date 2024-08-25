t = '#' + input()
p = '#' + input()


#겹치지 않도록 골라야 된다.

f = [0] * len(p)
f[0] = -1
for i in range(1, len(p)):
    j = f[i-1]

    while j>=0 and p[j+1] != p[i]:
        j = f[j]
    
    f[i] = j + 1


j = cnt = 0
for i in range(1, len(t)):
    while j >= 0 and p[j+1] != t[i]:
        j = f[j]
    
    j += 1
    if j == len(p) - 1:
        j = 0
        cnt += 1
print(cnt)