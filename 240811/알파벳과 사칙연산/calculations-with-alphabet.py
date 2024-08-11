def bact(depth, total):
    global word, result
    if depth == len(word) >> 1:
        result = max(result, total)
        return
    
    for i in range(1,5):
        bact(depth + 1, eval(f'{total}{word[(depth << 1)|1]}{i}'))

word = input()
result = -1 * (10 ** 10)
for i in range(1,5):
    bact(0,i)
print(result)