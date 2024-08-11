def bact(depth, total):
    global word, result
    if depth == len(word) >> 1:
        result = max(result, total)
        return
    op = word[(depth << 1)|1]
    for i in range(1,5):
        if op == '+':
            bact(depth + 1, total + i)
        elif op == '-':
            bact(depth + 1, total - i)
        else:
            bact(depth + 1, total * i)
        

word = input()
result = -1 * (10 ** 10)
for i in range(1,5):
    bact(0,i)
print(result)