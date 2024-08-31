import sys
input = sys.stdin.readline

n = int(input())

trie = {}

def insert(List):
    cur = trie
    for v in List:
        if cur.get(v, 0) == 0:
            cur[v] = {}
        cur = cur[v]
    cur['is_end'] = 1

def find(List):
    cur = trie
    for v in List:
        if cur.get(v, 0) == 0:return 0
        cur = cur[v]
    return cur.get('is_end', 0)


for _ in range(n):
    num, *List = input().split()
    insert(List)

def tree(cur, depth):
    for item in sorted(cur.keys()):
        if cur.get(item, 0) == 0 or item == 'is_end':continue
        print(f"{'--'*depth}{item}")
        tree(cur[item], depth + 1)
for item in sorted(trie.keys()):
    if item == 'is_end':continue
    print(item)
    tree(trie[item], 1)