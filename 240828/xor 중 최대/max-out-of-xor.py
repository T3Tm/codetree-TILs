import sys
input = sys.stdin.readline

def to_binary(n, result, depth = 0):
    if n < 2:
        result[depth] = f'{n%2}'
        return
    to_binary(n//2, result, depth + 1) 
    #최대 depth는 d이고 내가 depth 이기 때문에 하나하나 넣어주자
    result[depth] = f'{n%2}'

class Trie:
    def __init__(self, ):
        self.data = {}
        self.is_end = 0#현재 데이터 끝인지 확인
        self.end_point = 0
    def to_int(self,ch):
        return ord(ch) - ord('0')


    def insert(self, v,max_depth = 0 ,idx = 0):
        num = self.to_int(v[idx])
        if num not in self.data:#
            self.data[self.to_int(v[idx])] = Trie()#노드 생성
        if max_depth == idx + 1:#여기서 그만
            self.data[self.to_int(v[idx])].is_end += 1
        else:
            self.data[self.to_int(v[idx])].insert(v,max_depth,idx+1)
            
    def find(self, v, idx = 0):#해당 문자열 있는지 판단
        num = self.to_int(v[idx])
        if len(v) - 1 == idx:#있음
            return self.data[num].is_end > 0
        if num not in self.data:return 0
        return self.data[self.to_int(v[idx])].find(v,idx+1)
    
    def end_point(self):
        ret = 0
        for i in range(26):
            if self.data[i]:
                ret += self.data[i].end_point()
        self.end_point = ret + self.is_end
        return self.end_point

n = int(input())


root = Trie()
number = [*map(int, input().split())]
number_binary = []
for num in number:
    result = ['0']*32
    to_binary(num, result)
    number_binary.append(result[::-1])
    root.insert(number_binary[-1], 32)

def find(t: Trie, number, idx, result):
    global now,num
    #이 아이와 반대면서 비트 켜져 있는 아이들 한테로 들어가자
    number_int = int(number[idx]) ^ 1
    if idx + 1 == 32:#해당 곳에 값이 있는지 확인
        if number_int in t.data:#해당 데이터 있다면?
            if t.data[number_int].is_end:
                result += f'{number_int}'    
        else:
            if t.data[number_int^1].is_end:
                result += f'{number_int^1}'
        now = max(num ^ int(result,2),now)
        return
    
    if number_int in t.data:#있다면 그쪽으로 들어가서 최댓값 갖고 가기
        find(t.data[number_int], number, idx + 1, result + f'{number_int}')
    else:
        find(t.data[number_int^1], number, idx + 1, result + f'{number[idx]}')
result = 0
for i in range(n):
    num = number[i]
    now = 0
    #num과 반대 인 것 찾기
    find(root, number_binary[i], 0,'')
    result = max(result, now)
print(result)