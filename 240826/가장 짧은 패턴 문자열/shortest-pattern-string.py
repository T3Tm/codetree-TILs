import math
t = '#'+input() #어차피 제일 길어봤자 T임
#t를 2배 해놓고
#aabaabaab

f = [0] * len(t)
f[0] = -1
for i in range(1, len(t)):
    j = f[i-1]
    while j>=0 and t[j+1] != t[i]:
        j = f[j]
    
    f[i] = j + 1


left,right = 1, len(t)-1

while left<=right:#17번 
    mid = (left+right) >> 1
    pattern = '#' + t[1:mid+1]*math.ceil((len(t)-1)/mid)

    j = 0
    for i in range(1, min(len(t),len(pattern))):
        while j >= 0 and t[j+1]!=pattern[i]:
            j = f[j]
        j += 1
        if j == len(t) - 1:
            right = mid - 1
            break
    else:
        left = mid + 1
print(left)