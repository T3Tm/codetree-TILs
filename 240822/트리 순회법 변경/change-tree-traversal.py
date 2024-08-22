import sys
sys.setrecursionlimit(20002)
input = sys.stdin.readline

class Node:
    def __init__(self, value):
        self.parent = None
        self.left = None
        self.right = None
        self.value = value

def postorder(cur):
    if cur.left:
        postorder(cur.left)
    if cur.right:
        postorder(cur.right)
    print(cur.value)
def make_Tree(cur, value):
    if cur.value < value:#right으로 들어간다.
        if cur.right:
            make_Tree(cur.right, value)
        else:
            cur.right = Node(value)
            cur.right.parent = cur
    else:#왼쪽으로 가기
        if cur.left:
            make_Tree(cur.left, value)
        else:
            cur.left = Node(value)
            cur.left.parent = cur
n = int(input())

li = [int(input()) for _ in range(n)]
root = li[0]#루트 노드


cur = Node(root)#현재 커서
root = cur
for i in range(1,n):
    make_Tree(root, li[i])
postorder(root)