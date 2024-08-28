import sys
input = sys.stdin.readline
n = int(input())


class Trie:
    def __init__(self, ):
        self.data: [Trie] = [None] * 26
        self.is_end = 0#현재 데이터 끝인지 확인
        self.end_point = 0
    def to_int(self,ch):
        return ord(ch) - ord('0')


    def insert(self, v, idx = 0) -> bool:
        if self.data[self.to_int(v[idx])] == None:#
            self.data[self.to_int(v[idx])] = Trie()#노드 생성
        if len(v) == idx + 1:#여기서 그만
            self.data[self.to_int(v[idx])].is_end += 1
            for i in range(10):
                if self.data[self.to_int(v[idx])].data[i]:
                    return True
            return False
        else:
            ret = self.data[self.to_int(v[idx])].insert(v,idx+1)
            if self.data[self.to_int(v[idx])].is_end:
                ret = 1
            return ret
    def find(self, v, idx = 0):#해당 문자열 있는지 판단
        if len(v) - 1 == idx:#있음
            return self.data[self.to_int(v[idx])].is_end > 0
        if self.data[self.to_int(v[idx])] == None:return 0
        return self.data[self.to_int(v[idx])].find(v,idx+1)
    
    def end_point(self):
        ret = 0
        for i in range(26):
            if self.data[i]:
                ret += self.data[i].end_point()
        self.end_point = ret + self.is_end
        return self.end_point
    
root = Trie()

for _ in range(n):
    word = input().strip()
    ret = root.insert(word)
    if ret:
        print(0)
        break
else:
    print(1)