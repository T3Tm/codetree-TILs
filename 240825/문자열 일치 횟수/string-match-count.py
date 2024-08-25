n = int(input())
#p에서 n번 오른쪽으로 한칸씩 shift 하며, T와 일치하는 횟수를 구하자.
t = input()
t_len = len(t)
t = '#' + t * n
p = '#' + input()

p_len = len(p)

f = [0] * p_len
f[0] = -1

for i in range(1, p_len):
    j = f[i-1]
    
    while j>=0 and p[j+1] != p[i]:
        j = f[j]
    
    f[i] = j + 1

cnt = j = 0

for i in range(1, t_len + n):
    while j>=0 and p[j+1] != t[i]:
        j = f[j]
    
    j += 1
    if j == p_len - 1:
        j = f[j]
        cnt += 1
print(cnt)