n = int(input())
arr = [int(input()) for _ in range(n)]

answer = -21e8

def isCarry(num1, num2, num3):
    while num1 > 0 or num2 > 0 or num3 > 0:
        value1 = num1 % 10
        value2 = num2 % 10
        value3 = num3 % 10

        if value1 + value2 + value3 >= 10 : 
            return True
        
        num1 //= 10
        num2 //= 10
        num3 //= 10
    return False

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            num1 = arr[i]
            num2 = arr[j]
            num3 = arr[k]
            if not isCarry(num1, num2, num3):
                sum = num1 + num2 + num3
                answer = max(answer, sum)

print(answer)

 