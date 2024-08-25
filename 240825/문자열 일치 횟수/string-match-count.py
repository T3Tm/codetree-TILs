n = int(input())
t = '#' + input()
p = '#' + input()

p_len = len(p)
t_len = len(t)

f = [0] * p_len
f[0] = -1

for i in range(1, p_len):
    j = f[i-1]
    
    while j>=0 and p[j+1] != p[i]:
        j = f[j]
    
    f[i] = j + 1
cnt = 0
for start in range(1,n+1):
    j = 0
    point = start % p_len
    if not point:point = 1
    for i in range(1, t_len):
        while j>=0 and p[j+1] != t[point]:
            j = f[j]
        
        j += 1
        if j == p_len - 1:
            j = f[j]
            cnt += 1
            break
        point = (point + 1)%(p_len)
        if not point:point = 1
print(cnt)