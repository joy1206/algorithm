N = int(input())
heights = [int(input()) for _ in range(N)]

min_cost = 21e8

# 탐색 범위를 높이가 아닌 구간으로 넓힌다
for i in range(84):
    left = i
    right = i+ 17
    cost = 0
    for h in heights:
        if h < left :
            cost += (left - h) ** 2
        elif h > right:
            cost += (h - right) ** 2

    if min_cost > cost :
        min_cost = cost

print(min_cost)