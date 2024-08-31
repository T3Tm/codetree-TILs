import sys
sys.setrecursionlimit(200001)
input = sys.stdin.readline

n, m = map(int, input().split())

trie = {}


def insert(string):
    cur = trie
    for v in string:
        if cur.get(v, 0) == 0:
            cur[v] = {}
        cur = cur[v]
    cur[0] = 1#끝을 알리는 것
def find(string, result):
    cur = trie
    for idx in range(len(string)):
        if cur.get(string[idx], 0) == 0:break
        cur = cur[string[idx]]
        result[idx] = cur[1]
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

target = input().rstrip()
result = [0] * m
find(target, result)
print(*result)