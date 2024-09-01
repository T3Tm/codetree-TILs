import sys
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
    nexts = [*cur.keys()]
    if len(nexts) == 1:
        if nexts[0] != 0:
            find(cur[nexts[0]], now + nexts[0],cnt)
    elif len(nexts) == 2:
        if nexts[1] == 0:
            find(cur[nexts[0]], now + nexts[0],cnt)
        else:
            for j in nexts:
                if j == 0:continue
                find(cur[j],now + j, cnt + 1)
    else:    
        for j in nexts:
            if j == 0:continue
            find(cur[j],now + j, cnt + 1)
    if 0 in set(nexts):
        word[now] = cnt

arr = input().split()

for v in arr:
    insert(v)

find(trie, '',0)
for p in arr:
    print(word[p], end =' ')