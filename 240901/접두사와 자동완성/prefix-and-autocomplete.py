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
    ALL = set(cur.keys())
    next = ALL - {0}
    if len(next) == 1:#갈 곳이 한 곳밖에 없다면
        if 0 in ALL:
            find(cur[[*next][0]], now + [*next][0], cnt + 1)
        else:
            find(cur[[*next][0]], now + [*next][0], cnt )
    else:
        for nexts in next:
            find(cur[nexts],now + nexts, cnt + 1)
    
    if 0 in ALL:#여기서 끝나는 애들
        word[now] = cnt

arr = input().split()

for v in arr:
    insert(v)
for value in trie.keys():    
    find(trie[value], value, 1)

for p in arr:
    print(word[p], end=' ')