import sys

n, m = map(int, sys.stdin.readline().split())
numbers = [int(sys.stdin.readline()) for _ in range(n)]

while True:
    exploded = False
    temp = []

    i = 0
    while i < len(numbers):
        j = i
        while j < len(numbers) and numbers[j] == numbers[i]:
            j +=1
        if j - i < m :
            for k in range(i, j):
                temp.append(numbers[k])
        else:
            exploded = True
        i = j
    numbers = temp

    if not exploded or not numbers:
        break

print(len(numbers))
for i in range(len(nu)):
    print(numbers[i])