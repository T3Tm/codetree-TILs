import sys
sys.setrecursionlimit(1001)
input = sys.stdin.readline

n = int(input())

trie = {}

def insert(List):
    cur = trie
    for word in List:
        if cur.get(word, 0) == 0:
            cur[word] = {}
        cur = cur[word]
    cur[0] = 1

def prints(cur, depth):
    for key in sorted(filter(lambda x: x != 0,cur.keys())):
        if key == 0:continue
        print('--' * depth + key)
        prints(cur[key], depth + 1)


for _ in range(n):
    cnt, *List = input().split()
    insert(List)

prints(trie, 0)