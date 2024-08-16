import sys
input = sys.stdin.readline
class Node:
    def __init__(self, data):
        self.data = data # Linked list의 노드에 담을 데이터
        self.prev = None       # 초기에는 이전 노드와 다음 노드가 존재하지 않는다.
        self.next = None

def insert_next(u, singleton):
    # singleton의 prev와 next를 설정
    singleton.prev = u
    singleton.next = u.next

    # singleton의 이전 노드의 next와
    # 다음 노드의 prev를 설정       
    if singleton.prev is not None:
        singleton.prev.next = singleton
    if singleton.next is not None:
        singleton.next.prev = singleton

def insert_prev(u, singleton):
    singleton.prev = u.prev
    singleton.next = u
    
    # singleton의 이전 노드의 next와
    # 다음 노드의 prev를 설정
    if singleton.prev is not None:
        singleton.prev.next = singleton
    if singleton.next is not None:
        singleton.next.prev = singleton

def pop(u):
    # u의 이전 노드와 다음 노드를 서로 이어줌
    if u.prev is not None:
        u.prev.next = u.next
    if u.next is not None:
        u.next.prev = u.prev

    # 이제, u는 단일 노드가 됨
    u.prev = u.next = None

head = Node(input().strip())
n = int(input())
output = ''
for _ in range(n):
    cmd, *word = input().split()

    if cmd == '1':
        insert_prev(head, Node(word[0]))
    elif cmd == '2':
        insert_next(head, Node(word[0]))
    elif cmd == '3':
        if head.prev:
            head = head.prev
    else:
        if head.next:
            head = head.next
    
    a,b,c = head.prev,head,head.next
    r = ''
    if a:
        r += f'{a.data} '
    else:
        r += '(Null) '
    
    r += f'{b.data} '

    if c:
        r += f'{c.data}'
    else:
        r += '(Null)'
    
    output += f'{r}\n'
print(output)