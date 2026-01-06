n, m, p = map(int, input().split())
messages = []

for _ in range(m):
    c, u = input().split()
    messages.append((c, int(u)))
                
def solution():
    target_u = messages[p-1][1]

    if target_u == 0:
        return

    readers = set()
    
    for i in range(m):
        if messages[i][1] == target_u or i >= p - 1:
            readers.add(messages[i][0])

    for i in range(n):
        person = chr(ord('A') + i)
        if person not in readers:
            print(person, end=" ")
solution()