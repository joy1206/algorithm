n = int(input())
arr = list(map(int, input().split()))

arr.sort()

num1 = arr[0] * arr[1] * arr[-1]
num2 = arr[-1] * arr[-2] * arr[-3]

print(max(num1, num2))