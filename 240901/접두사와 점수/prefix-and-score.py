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
    cur[0] = 1#끝을 알리는 것
def find(cur, depth):
    global result
    result = max(result, depth * cur[1])
    for key in cur.keys():
        if key == 0 or key == 1:continue
        find(cur[key], depth + 1)
def preProcessing(cur):
    #해당 cur에는 단어가 총 몇개 있는지 확인하기
    cur[1] = cur.get(0, 0)
    for key in cur.keys():
        if key == 1 or key == 0:continue
        cur[1] = cur[1] + preProcessing(cur[key])
    return cur[1]
for word in input().split():
    insert(word)

for key in trie.keys():
    preProcessing(trie[key])

result = 0
for key in trie.keys():
    find(trie[key], 1)#현재 한 글자
print(result)