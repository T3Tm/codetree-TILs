from math import ceil

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def isEmpty(self):
        return self.head == None
    
    def insertBegginning(self, newNode):
        if self.head == None:
            self.head = newNode
            self.tail = newNode
            return
        self.insertBefore(self.head, newNode)
    def insertBefore(self, prev, next):
        next.next = prev
        if prev.prev == None:#헤드 노드
            self.head = next
            prev.prev = next
            return
        prev.prev.next = next
        next.prev = prev.prev
        prev.prev = next
    def insertEnd(self, newNode: Node):
        if self.tail == None:
            self.head = newNode
            self.tail = newNode
            return
        self.insertAfter(self.tail, newNode)
    def insertAfter(self, node: Node, newNode: Node):
        newNode.prev = node
        if node.next == None:
            self.tail = newNode
            node.next = newNode    
            return
        newNode.next = node.next
        node.next.prev = newNode
        node.next = newNode
    def remove(self,node: Node):
        if node.prev != None:
            node.prev.next = node.next
        else:
            if node.next != None:
                node.next.prev = None
            self.head = node.next
        
        if node.next != None:
            node.next.prev = node.prev
        else:
            if node.prev != None:
                node.prev.next = None
            self.tail = node.prev
#n명의 사람들이 M개의 여러 줄에 나눠서 줄을 서고 있다.

#1 a b a인 사람이 b사람 새치기했음.
#2 a a가 집으로 갔음
#3 이름이 a부터 b인 사람이 통째로 c인 사람 앞으로 새치기 했음
n, m, q = map(int,input().split())

x = n // m # 2

li = input().split()
cache = [[' ']*(x+1) for _ in range(m+1)]
result = [DoubleLinkedList() for _ in range(m+1)]
for i in range(1,n+1):
    value = li[i-1]
    row = ceil(i/x)
    cache[row][(i-1)%x + 1] = value

for i in range(1,m+1):
    for j in range(1,x+1):
        if cache[i][j] == ' ':break
        node = Node(cache[i][j])
        result[i].insertEnd(node)

#a인 사람 찾기

for _ in range(q):
    cmd, n1, *n2 = input().split()
    if cmd == '1':
        n3 = ''
        n4 = ''
        for i in range(1, m+1):
            node = result[i].head

            while node:
                if node.value == n1:
                    result[i].remove(node)
                    n3 = node
                elif node.value == n2[0]:
                    #이 노드에다가 넣어야 됨.
                    n4 = (result[i], node)
                    break
                node = node.next
        n4[0].insertBefore(n4[1], n3)
    elif cmd == '2':#이 사람은 집을 갔다는 것은 노드에서 빼야됨.
        for i in range(1,m+1):#행을 돌면서 해당 숫자 찾기
            node = result[i].head
            
            while node and node.value != n1:
                node = node.next
            if node and node.value == n1:#찾았음
                result[i].remove(node)#이 노드 삭제하기
                break
    else:
        n3 = ''
        n4 = ''
        temp = []
        for i in range(1, m + 1):
            node = result[i].head

            while node:
                if node.value == n1:
                    while node and node.value != n2[0]:
                        n1 = node.next
                        temp.append(node.value)#넣어야할 이름들 적어놓기
                        result[i].remove(node)
                        node = n1
                    result[i].remove(node)
                    break
                elif node.value == n2[1]:
                    n4 = (result[i], node)
                    break
        for name in temp[::-1]:
            node = Node(name)
            n4[0].insertBefore(n4[1], node)
            n4[1] = node
            
        

for i in range(1,m+1):
    head = result[i].head
    while head != None:
        print(head.value, end=' ')
        head = head.next
    print()