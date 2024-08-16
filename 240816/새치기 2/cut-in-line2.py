from math import ceil
from collections import deque
import sys
input = sys.stdin.readline

n, m, q = map(int,input().split())

li = [*input().split()]

x = n//m #2이다.

cache = [deque() for _ in range(m)]
for i in range(1,n+1):
    row = ceil(i / x) - 1
    column = (i-1)%x 
    cache[row].append(li[i-1])

def find(name):
    for row in range(m):
        for column in range(len(cache[row])):
            if cache[row][column] == name:#찾았음
                return [row, column]
for _ in range(q):
    cmd, a, *b = input().split()
    if cmd == '1':
        #a와 b의 행과 열 찾아주기
        a_result = find(a)
        #a를 꺼낼 것인데 column이 뒤가 가까운지 앞이 가까운지 체크
        if len(cache[a_result[0]]) >> 1 > a_result[1]:
            #앞이 더 가깝기 때문에 a_result[1]까지 다 빼내기
            temp = []
            for _ in range(a_result[1]-1):
                temp.append(cache[a_result[0]].popleft())
            cache[a_result[0]].popleft()#자기 자신까지 나오기
            while temp:
                name = temp.pop()
                cache[a_result[0]].appendleft(name)
        else:
            temp = []
            for _ in range(len(cache[a_result[0]])-a_result[1]-1):
                temp.append(cache[a_result[0]].pop())
            cache[a_result[0]].pop()#자기 자신까지 나오기
            while temp:
                name = temp.pop()
                cache[a_result[0]].append(name)
        
        b_result = find(b[0])
        if len(cache[b_result[0]]) >> 1 > b_result[1]:
            #앞으로 빼는 것이 더 빠름
            temp = []
            for _ in range(b_result[1]-1):
                temp.append(cache[b_result[0]].popleft())
            cache[b_result[0]].appendleft(a)#a를 넣기
            while temp:#다시 원복
                name = temp.pop()
                cache[b_result[0]].appendleft(name)
        else:
            temp = []
            for _ in range(len(cache[b_result[0]])-b_result[1]):
                temp.append(cache[b_result[0]].pop())
            cache[b_result[0]].append(a)#a를 넣기
            while temp:#다시 원복
                name = temp.pop()
                cache[b_result[0]].append(name)
    elif cmd == '2':
        a_result = find(a)
        if len(cache[a_result[0]]) >> 1 > a_result[1]:
            #앞이 더 가깝기 때문에 a_result[1]까지 다 빼내기
            temp = []
            for _ in range(a_result[1]-1):
                temp.append(cache[a_result[0]].popleft())
            cache[a_result[0]].popleft()#자기 자신까지 나오기
            while temp:
                name = temp.pop()
                cache[a_result[0]].appendleft(name)
        else:
            temp = []
            for _ in range(len(cache[a_result[0]])-a_result[1]-1):
                temp.append(cache[a_result[0]].pop())
            cache[a_result[0]].pop()#자기 자신까지 나오기
            while temp:
                name = temp.pop()
                cache[a_result[0]].append(name)
                
    else:#a에서 b인원 통째로 c 앞으로 새치기
        a_result = find(a)
        b_result = find(b[0])
        
        if a_result[1] + 1 > len(cache[b_result[0]]) - b_result[1]:
            #뒤로 빼는 것이 무조건 이득
            temp = []
            while cache[b_result[0]] and cache[b_result[0]][-1] != b[0]:
                temp.append(cache[b_result[0]].pop())
            
            save = []

            while cache[a_result[0]] and cache[a_result[0]][-1] != a:
                save.append(cache[a_result[0]].pop())
            
            if cache[a_result[0]]:
                save.append(cache[a_result[0]].pop())#자기 자신까지 저장
            #temp에 있는 것은 다시 넣어놓아야 함.
            while temp:cache[a_result[0]].append(temp.pop())
            
            
            c_result = find(b[1])
            if len(cache[c_result[0]]) >> 1 > c_result[1]:#앞으로 빼서 넣는 것이 더 이득
                tt = []
                while cache[c_result[0]] and cache[c_result[0]][0] != b[1]:
                    tt.append(cache[c_result[0]].popleft())

                while save:
                    cache[c_result[0]].appendleft(save.pop())
            else:
                tt = []
                while cache[c_result[0]] and cache[c_result[0]][-1] != b[1]:
                    tt.append(cache[c_result[0]].pop())
                
                l = cache[c_result[0]].pop()#자기 자신 빼야됨.
                                
                while save:
                    cache[c_result[0]].append(save.pop())
                

                cache[c_result[0]].append(l)
                
        else:
            #앞으로 빼야됨.
            temp = []
            while cache[a_result[0]] and cache[a_result[0]][0] != a:
                temp.append(cache[a_result[0]].popleft())
            
            save = []

            while cache[b_result[0]] and cache[b_result[0]][0] != b[0]:
                save.append(cache[b_result[0]].popleft())
            if cache[b_result[0]]:
                save.append(cache[b_result[0]].popleft())#b 자기 자신까지 저장
            #temp에 있는 것은 다시 넣어놓아야 함.
            while temp:cache[b_result[0]].appendleft(temp.pop())
            
            c_result = find(b[1])
            if len(cache[c_result[0]]) >> 1 > c_result[1]:#앞으로 빼서 넣는 것이 더 이득
                tt = []
                while cache[c_result[0]] and cache[c_result[0]][0] != b[1]:
                    tt.append(cache[c_result[0]].popleft())

                while save:
                    cache[c_result[0]].appendleft(save.pop())
            else:
                tt = []
                while cache[c_result[0]] and cache[c_result[0]][-1] != b[1]:
                    tt.append(cache[c_result[0]].pop())
                
                l = cache[c_result[0]].pop()
                
                while save:
                    cache[c_result[0]].append(save.pop())
                
                cache[c_result[0]].append(l)
for i in range(m):
    if cache[i]:
        print(*cache[i])
    else:
        print(-1)
#5만