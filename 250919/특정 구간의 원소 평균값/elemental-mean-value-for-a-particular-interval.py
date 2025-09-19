n = int(input())
arr = list(map(int, input().split()))

answer = 0

for i in range(n):
    for j in range(i, n):
        num= 0
        length = j - i + 1
        for k in range(i, j+1):
            num += arr[k]

        average = num / length
        for l in range(i, j +1):
            if arr[l] == average:
                answer += 1
                break
print(answer)