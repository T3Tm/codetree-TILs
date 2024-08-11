n,m,t = map(int,input().split())
class bead:
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    trans = {'R':0,'L':1,'D':2,'U':3}
    def __init__(self, x,y ,dir, w, n = 0):
        self.x = x
        self.y = y
        self.dir = self.trans.get(dir,dir)
        self.w = w
        self.n = n
    def turn(self):
        if self.dir == 0:
            self.dir = 1
        elif self.dir == 1:
            self.dir = 0
        elif self.dir == 2:
            self.dir = 3
        else:
            self.dir = 2
    def move(self):
        nx = self.x + bead.dx[self.dir]
        ny = self.y + bead.dy[self.dir]
        if nx < 1 or nx > n or ny < 1 or ny > n:
            #자기 자신 자리에서 dir만 변화
            self.turn()
        else:
            self.x = nx
            self.y = ny
board = [[set() for _ in range(n+1)] for _ in range(n+1)]

beadList = {}
for idx in range(m):
    r,c,d,w = input().split()
    r,c,w = map(int, [r,c,w])
    beadList[idx] = bead(r,c,d,w,n)
    board[r][c].add(idx)

for _ in range(t):
    for idx,beads in beadList.items():
        board[beads.x][beads.y].remove(idx)
        beads.move()
        board[beads.x][beads.y].add(idx)
    
    #같은 곳에 여러 개의 구슬 있는지 확인
    for i in range(1,n+1):
        for j in range(1,n+1):
            if len(board[i][j]) > 1:
                #구슬을 하나로 합쳐야 되는데
                #가장 큰 idx 알아내기
                idx = max(board[i][j])
                weight = 0
                d = beadList[idx].dir
                for idxs in board[i][j]:
                    weight += beadList[idxs].w
                    beadList.pop(idxs)
                beadList[idx] = bead(i,j,d,weight,n)

                board[i][j] = set([idx])
values = beadList.values()
print(len(values), max([*map(lambda x:x.w,values)]))