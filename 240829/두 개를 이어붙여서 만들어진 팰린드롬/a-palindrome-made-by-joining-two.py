n = int(input())
arr = input().split()

result = 0
for t in range(n-1):
    for m in range(t+1,n):
        word = '#'+ '#'.join(arr[t] + arr[m])+'#'
        words = '#'+'#'.join(arr[m] + arr[t]) + '#'
        
        A = [0] * len(word)
        AA = [0] * len(words)
        #마나커 알고리즘
        r = q = -1
        for i in range(1, len(word)):
            if r >= i:
                ii = 2 * q - i
                A[i] = min(r-i, A[ii])
            while i - A[i] - 1 >=0 and i + A[i] + 1 < len(word) and \
                word[i - A[i] - 1] == word[i + A[i] + 1]:
                    A[i]+=1
            if i + A[i] > r:
                r, q = i + A[i], i
        
        if 2*A[len(word)//2]+1 == len(word):#이 곳의 값이 반지름인지 확인
            result = max(result, len(word)//2)
        r = q = -1
        for i in range(1, len(words)):
            if r >= i:
                ii = 2 * q - i
                AA[i] = min(r-i, AA[ii])
            while i - AA[i] - 1 >=0 and i + AA[i] + 1 < len(words) and \
                words[i - AA[i] - 1] == words[i + AA[i] + 1]:
                    AA[i]+=1
            if i + AA[i] > r:
                r, q = i + AA[i], i
        if 2*AA[len(words)//2]+1 == len(words):#이 곳의 값이 반지름인지 확인
            result = max(result, len(words)//2)
print(result)