abilities = list(map(int, input().split()))

def get_diff(i, j):
    sum1 = abilities[i] + abilities[j]
    sum2 = sum(abilities)- sum1
    return abs(sum1-sum2)

min_diff = 21e8
for i in range(0, 6):
    for j in range(i+1, 6):
        min_diff = min(min_diff, get_diff(i, j))
print(min_diff)