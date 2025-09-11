n = int(input())
numbers = list(map(int, input().split()))

answer = -21e8

for i in range(n-2):
    for j in range(i+2, n):
        num = 0
        num += numbers[i] + numbers[j]
    answer = max(num, answer)
print(answer)


