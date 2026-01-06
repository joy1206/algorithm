n, m, p = map(int, input().split())
messages = [tuple(input().split()) for _ in range(m)]

p_read = [False] * m


for i in range(n):
    if i >= p-1:
        p_read[ord(messages[i][0])-65] = True

for i in range(m):
    if p_read[i] == False:
        print(chr(i+65), end=" ")
