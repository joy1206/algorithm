T, a, b = map(int, input().split())
c = []
x = []
ans = 0
for _ in range(T):
    char, pos = input().split()
    c.append(char)
    x.append(int(pos))

for i in range(a, b+1):
    d1, d2 = 1000, 1000
    for j in range(T):
        if c[j] == 'S':
            temp = abs(x[j]-i)
            d1 = min(d1, temp)
        else:
            temp = abs(x[j]-i)
            d2 = min(d2, temp)
    if d1 <= d2: 
        ans +=1

print(ans)
