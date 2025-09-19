n, k = map(int, input().split())
x = []
c = []
score = -21e8
for _ in range(n):
    pos, char = input().split()
    x.append(int(pos))
    c.append(char)

end = max(x)
arr =  [0 for _ in range(end)]
alphabet = [0 for _ in range(end)]

for num in range(n):
    index = x[num]
    arr[index-1] = 1
    alphabet[index-1] = c[num]

for i in range(end-k):
    temp = 0
    for j in range(k+1):
        if arr[i+j] == 1:
            if alphabet[i+j] == 'G':
                temp += 1
            elif alphabet[i+j] == 'H':
                temp += 2
    if score < temp:
        score = temp
print(score)

