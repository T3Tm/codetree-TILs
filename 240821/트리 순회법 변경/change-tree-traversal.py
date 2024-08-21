import sys
sys.setrecursionlimit(20002)
input = sys.stdin.readline

n = int(input())

#전위 순회한 결과가 주어졌다.

#이것을 후위 순회로 고쳐라.

#전위 순회 : 부모, 왼쪽, 오른쪽
li = [int(input()) for _ in range(n)]
root = li[0]#루트 노드

class Node:
    def __init__(self, value):
        self.parent = None
        self.left = None
        self.right = None
        self.value = value

tree = Node(root)#root부터 시작하는 트리 시작

idx = 1#현재 놓아야 될 아이
def makeTree(cur, parent):
    global idx
    if idx == n:return
    cur.parent = parent#자신의 부모의 번호 넣어주기
    now_value = li[idx]#현재 놓아야할 값
    if cur.value > now_value:#그냥 단순히 왼쪽으로 넣어주면 된다.
        cur.left = Node(now_value)#나의 왼쪽으로 넣어주고
        idx += 1
        makeTree(cur.left, cur)#왼쪽으로 들어가기
    else:#내 값보다 크다면
        if parent.value < now_value:#이러면 부모로 들어가서 만들어주기
            makeTree(parent, parent.parent)
        else:#부모 보다는 작다면 현재 위치에 있어도 되고
            cur.right = Node(now_value)
            idx += 1
            makeTree(cur.right, cur)

def postorder(cur):
    if cur.left:
        postorder(cur.left)
    if cur.right:
        postorder(cur.right)
    print(cur.value)

makeTree(tree, Node(1000001))

postorder(tree)