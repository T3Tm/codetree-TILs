n, word = input().split()
n = int(n)

cnt = {}#해당 해시 갯수 세주기

p = [31, 37]
m = [10**7, 10**9]

p_pow= [[]for _ in range(2)]#싹 구해주기

for k in range(2):
    p_pow[k].append(1)
    for i in range(1,n):
        p_pow[k].append((p_pow[k][-1] * p[k])%m[k]) 
def to_int(ch):
    return ord(ch) - ord('a') + 1

word_hash = [0,0]
for k in range(2):
    for i in range(n):
        word_hash[k] = (word_hash[k] + to_int(word[i]) * p_pow[k][n - i - 1]) % m[k]

cnt[tuple(word_hash)] = 1

for i in range(1,len(word) - n + 1):
    for k in range(2):
        word_hash[k] = ((word_hash[k] - to_int(word[i-1]) * p_pow[k][-1])*p[k] + to_int(word[i+n-1]) + m[k]) %m[k]
    
    cnt[tuple(word_hash)] = cnt.get(tuple(word_hash), 0) + 1

print(max(cnt.values()))