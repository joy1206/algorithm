N, K = map(int, input().split())
num = [int(input()) for _ in range(N)]
exploded = [False]*N

for i in range(N):
    for j in range(i+1, min(i+K+1, N)):
        if num[i] == num[j]:
            exploded[i] = True
            exploded[j] = True

bomb_counts = {}
for i in range(N):
    if exploded[i]:
        bomb_num = num[i]
        bomb_counts[bomb_num] = bomb_counts.get(bomb_num, 0) + 1

max_count = 0
max_num = 0

for bomb_num, count in bomb_counts.items():
    if count > max_count :
        max_count = count
        max_num = bomb_num
    elif count == max_count:
        max_num = max(max_num, bomb_num)

print(max_num)
    