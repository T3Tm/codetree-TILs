n = int(input())

t = '#' + input()
p = '#' + input() * 2

t_len = len(t) #100000
p_len = len(p) #200000



f = [0] * t_len
f[0] = -1
for i in range(1, t_len):
    j = f[i-1]
    while j >= 0 and t[j+1] != t[i]:
        j = f[j]
    
    f[i] = j + 1

j = cnt = 0
for i in range(1, p_len-1):
    while j>=0 and p[j+1]!=p[i]:
        j = f[j]
    j+= 1
    if j == t_len - 1:
        cnt += 1
        j = f[j]
print(cnt)