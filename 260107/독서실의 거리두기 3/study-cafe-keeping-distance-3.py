N = int(input())
seats = input()

# 가장 먼 1간의 쌍 찾기
min_dist = 21e8
max_dist = 0
for i in range(N):
    if seats[i] == '1':
        for j in range(i+1, N):
            if seats[j] == '1':
                max_dist = max(max_dist, j-i)
                min_dist = min(min_dist, j-i)
                break

if min_dist == 1:
    print(1)
else:
    print(max_dist//2)