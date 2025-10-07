X, Y = map(int, input().split())

max_sum = 0

cnt = 0
for i in range(X, Y+1):
    current_num = str(i)
    sum_of_digits = sum(int(j)for j in current_num)
    max_sum = max(max_sum, sum_of_digits)
print(max_sum)

