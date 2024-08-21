n = int(input())
#최대한 많이 잡아서 바꾸면 되지 않을까
#일단 현재 다르다면 바꿔야 된다.

#
word = [*input()]
target = [*input()]
cnt = 0
i = 0
while i < n:
    #i부터 4개까지 보고 최대한 계속 뒤집는다.
    j = 0
    while i + j < n and j < 4:
        if word[i+j] == target[i+j]:
            break
        j += 1
    if j:#있으면 4개씩
        cnt += 1
        i = i + j
    else:
        i+=1
print(cnt)