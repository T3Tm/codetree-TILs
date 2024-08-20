import sys
from math import ceil
input = sys.stdin.readline
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

def insertBefore(node, new_node):
    new_node.next = node

    if not node.prev:
        node.prev = new_node
        return
    new_node.prev = node.prev
    node.prev.next = new_node
    node.prev = new_node

def insertAfter(node, new_node):
    #node 이후로 추가하기
    new_node.prev = node
    if not node.next:
        node.next = new_node
        return
    #이미 있던 것은 뒤로 밀려나야 된다.
    new_node.next = node.next
    node.next.prev = new_node
    node.next = new_node

def remove(node):#해당 노드 지우기
    #이전과 이후를 연결해줘야됨.
    if node.prev:
        node.prev.next = node.next#내가 원래 다음으로 가리키고 있던 것을 이전이 가리키게 끔
    if node.next:
        node.next.prev = node.prev
    
n, m, q = map(int,input().split())

#1번 행
#2번 행
x = n // m
board = [Node(i)for i in range(m)]
tail = [board[i]for i in range(m)]

dic = {}
for idx, name in enumerate(input().split(),1):
    row = ceil(idx/x)-1
    dic[name] = Node(name)
    insertAfter(tail[row], dic[name])
    tail[row] = tail[row].next

for _ in range(q):
    cmd,a,*b = input().split()
    if cmd == '1':
        n = dic[a]
        remove(n)
        l = dic[b[0]]
        insertBefore(l, n)
    elif cmd == '2':
        remove(dic[a])
    else:#3번의 앞에 
        l = dic[b[0]]
        p = dic[b[1]]
        while l and l.value != a:
            tmp = l.prev
            remove(l)
            insertBefore(p, l)
            l = tmp
            p = p.prev
        remove(l)
        insertBefore(p, l)

for i in range(m):
    head = board[i].next
    while head:
        print(head.value, end =' ')
        head = head.next
    if not board[i].next:
        print(-1)
    else:
        print()