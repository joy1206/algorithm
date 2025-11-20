A, B, C = map(int, input().split())

max_num = 0

for i in range(C//A +1):
    for j in range(C//B +1):
        num = 0
        num += A *i + B * j
        if num <= C:
            max_num = max(max_num, num)
print(max_num)
