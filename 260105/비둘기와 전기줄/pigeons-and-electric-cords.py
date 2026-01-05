N = int(input())
pigeon = {}
position = []
ans = 0
for _ in range(N):
    p, pos = map(int, input().split())
    if p not in pigeon:
        pigeon[p] =[]
    pigeon[p].append(pos)

for p, pos in pigeon.items():
    for i in range(len(pos)-1):
        if pos[i] != pos[i+1]:
            ans +=1
print(ans)