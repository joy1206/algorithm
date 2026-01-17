n = int(input())
blocks = [int(input()) for _ in range(n)]

target = sum(blocks)//n

ans = 0

for i in range(n):
    if blocks[i] < target:
        ans += target - blocks[i]
print(ans)
        
