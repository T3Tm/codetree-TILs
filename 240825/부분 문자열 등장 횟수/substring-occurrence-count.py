#rabin karp, kmp 

# 문자열이 있을 때 부분 문자열이 어디서 일치하지는 알아내는 알고리즘
t = '#' + input()
p = '#' + input()

f = [0] * (len(p))
f[0] = -1
for i in range(1, len(p)):
    j = f[i-1]
    
    while j>=0 and p[j+1] != p[i]:
        j = f[j]

    f[i] = j + 1

j = 0
cnt = 0
for i in range(1, len(t)):
    
    while j >= 0 and p[j+1] != t[i]:
        j = f[j]
    
    j += 1 
    if j == len(p) - 1:
        cnt += 1
        j = f[j]

print(cnt)