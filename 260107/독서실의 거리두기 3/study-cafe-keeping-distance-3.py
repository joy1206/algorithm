N = int(input())
seats = input()

# 가장 먼 1간의 쌍 찾기
max_dist = 0
left, right = 0, 0
for i in range(N):
    if seats[i] == '1':
        for j in range(i+1, N):
            if seats[j] == '1':
                max_dist = max(max_dist, j-i)
                left = i
                right = j
                break

print(max_dist//2)
