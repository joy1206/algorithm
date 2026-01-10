a = list(map(int, input().split()))
a.sort()

# 한 칸씩 옮기지 말고 먼저 거리를 계산 후 최대값 구하기
gap1 = a[1] - a[0] -1
gap2 = a[2] - a[1] -1
print(max(gap1, gap2))