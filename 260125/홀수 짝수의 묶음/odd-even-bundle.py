import sys

n = int(input())
numbers = list(map(int, input().split()))

even = 0
odd = 0
for x in numbers:
    if x % 2 == 0:
        even += 1
    else:
        odd += 1

while odd > even:
    odd -= 2
    even += 1

if even > odd + 1:
    even = odd + 1

print(even + odd)