ability = list(map(int, input().split()))

ability.sort()

num1 = ability[-1] + ability[0]
num2 = ability[-2] + ability[1]
num3 = ability[-3] + ability[2]

print(max(num1, num2, num3) - min(num1, num2, num3))

