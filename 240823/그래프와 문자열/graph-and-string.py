import sys
input = sys.stdin.readline
n, s = input().split()
n = int(n)

def to_int(ch):
    return ord(ch) - ord('a') + 1

# n - 1개
def dfs(cur, depth, w1 , w2):
    global result, target_len

    now_hash = [w1, w2]
    
    if depth > target_len:
        for k in range(2):
            now_hash[k] = ((now_hash[k] - to_int(pick[depth - target_len - 1]) * p_pow[k][target_len-1])*p[k] + to_int(pick[depth-1]) + m[k])%m[k]

    elif depth == target_len:
        for k in range(2):
            for i in range(target_len):
                now_hash[k] = (now_hash[k] + to_int(pick[i]) * p_pow[k][target_len - i - 1])%m[k]
    
    if now_hash == target_hash:
        result += 1

    for next, value in graph[cur]:
        pick[depth] = value
        dfs(next, depth + 1, now_hash[0], now_hash[1])

graph = [[]for _ in range(n+1)]
for _ in range(n-1):
    a,b,c = input().split()
    a,b = int(a), int(b)
    graph[a].append((b,c))

p = [31, 37]
m = [10**9 + 7, 10**9 + 9]
p_pow = [
    [0] * (n + 1)
    for _ in range(2)
]

for k in range(2):
    p_pow[k][0] = 1
    for i in range(1, n+1):
        p_pow[k][i] = (p_pow[k][i-1] * p[k]) % m[k]

target_len = len(s)
target_hash = [0, 0]
for k in range(2):
    for i in range(target_len):
        target_hash[k] = (target_hash[k] + to_int(s[i])*p_pow[k][target_len - i - 1])%m[k]

result = 0

pick = [0] * (n+1)
dfs(1, 0, 0 , 0)#n-1번

print(result)