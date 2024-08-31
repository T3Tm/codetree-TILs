#n개의 단어
#4 x 4

#단어 n개를 입력 받아서 일단 저장
import sys
input = sys.stdin.readline
#2. dfs를 돌려서 해당 칸에서 다른 칸으로 가게끔 만들기
trie = {}
def c2i(char):
    return ord(char) - ord('a')
def insert(string):
    global unused
    cur = trie
    for v in string:
        if cur.get(c2i(v), 0) == 0:
            cur[c2i(v)] = {}#새로 하나 만들기
        cur = cur[c2i(v)]
    cur['is_end'] = 1#여기에서 끝남

def find(string):
    cur = trie
    for v in string:
        if cur.get(c2i(v), 0) == 0:
            return 2
        cur = cur[c2i(v)]
    return cur.get('is_end', 0)
    
def dfs(x, y, word, depth):#
    global result
    ret = find(word)#이거 없으면 리턴
    if ret == 2:#다음은 아예 없음
        return
    #해당 곳에
    elif ret == 1:#최장 길이 체크 
        result = max(result, len(word))
    if depth == 8:return
    for dx, dy in (0,1),(0,-1),(1,0),(-1,0),(-1,1),(-1,-1),(1,1),(1,-1):
        nx,ny = x +dx, y +dy
        if nx < 0 or nx>=4 or ny < 0 or ny>=4:continue
        if visited[nx][ny]:continue
        visited[nx][ny] = 1
        dfs(nx,ny,word+board[nx][ny], depth + 1)
        visited[nx][ny] = 0
n = int(input())
for data in input().split():
    insert(data)
board = [input().rstrip() for _ in range(4)]

visited = [[0]*4 for _ in range(4)]
result = 0
for i in range(4):
    for j in range(4):
        visited[i][j] = 1
        dfs(i,j, board[i][j], 0)#여기서 부터 시작해서 만들기
        visited[i][j] = 0
print(result)