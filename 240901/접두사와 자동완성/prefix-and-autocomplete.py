import sys
sys.setrecursionlimit(200001)
input = sys.stdin.readline

n = int(input())
trie = {}

def insert(string):
    cur = trie
    for v in string:
        if cur.get(v, 0) == 0:
            cur[v] = {}
        cur = cur[v]
    cur[0] = 1#끝났다는 걸 표현

word = {}#각 단어에 맞게 몇 개씩 검색해야 되는지 
def find(cur, now, cnt):
    nexts = set(cur.keys())
    
    for k in nexts:
        if k == 0:continue#끝
        
        if len(nexts) == 1:
            find(cur[k], now + k, cnt)
        elif len(nexts) == 2:
            if 0 in nexts:
                find(cur[k], now + k,cnt)
            else:
                find(cur[k], now +k,cnt+1)
        else:
            find(cur[k], now +k,cnt+1)
    
    if 0 in nexts:
        word[now] = cnt

arr = input().split()

for v in arr:
    insert(v)
for value in trie.keys():    
    find(trie[value], value, 1)
for p in arr:
    print(word[p], end =' ')