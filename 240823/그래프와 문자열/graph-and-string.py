import sys
sys.setrecursionlimit(100002)
input = sys.stdin.readline
n, s = input().split()
n = int(n)
'''
노드 n개와 n-1개의 간선으로 이뤄진 그래프가 있다.

각 간선에는 소문자 알파벳이 하나씩 적혀있으며,

방향 그래프 

dfs(1)

목적 S 문자열이 존재
1 -> 2 a
    2 -> 4 ab
        4 -> 5 abb

1 -> 6 b
    6 -> 7 ba
        7 -> 3 bab
        7 -> 8 bac
'''
# n - 1개
def rabin_karp(word, t):
    if len(word) < target_len:return
    word_hash = [0,0]

    for i in range(target_len):
        for k in range(2):
            word_hash[k] = (word_hash[k] + to_int(word[i])*p_pow[k][target_len - i - 1])%m[k]
    
    if word_hash == target_hash:
        result[t[0]] = 1
    
    
    for i in range(1, len(word) - target_len + 1):
        for k in range(2):
            word_hash[k] = ((word_hash[k] - to_int(word[i-1]) * p_pow[k][-1])*p[k] + to_int(word[i + target_len - 1]) + m[k])%m[k]

        if word_hash == target_hash:
            result[t[i]] = 1


def dfs(cur, word, t):
    global result
    visited[cur] = 1
    if not len(graph[cur]):
        rabin_karp(word, t)#n
    for next, value in graph[cur]:
        if visited[next]:continue
        t.append(next)
        dfs(next, word + value, t)
        t.pop()

graph = [[]for _ in range(n+1)]
for _ in range(n-1):
    a,b,c = input().split()
    a,b = int(a), int(b)
    graph[a].append((b,c))

p = [31, 37]
m = [10**9 + 7, 10**9 + 9]
p_pow = [[1]for _ in range(2)]
for k in range(2):
    for _ in range(1, len(s)):
        p_pow[k].append((p_pow[k][-1] * p[k]) % m[k])


def to_int(ch):
    return ord(ch) - ord('a') + 1

target_len = len(s)
target_hash = [0, 0]
for i in range(target_len):
    for k in range(2):
        target_hash[k] = (target_hash[k] + to_int(s[i])*p_pow[k][target_len - i - 1])%m[k]


visited=[0] * (n+1)
result = [0] * (n+1)
dfs(1,'', [])#n-1번

print(sum(result))