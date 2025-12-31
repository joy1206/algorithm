n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
x1, x2 = zip(*segments)
x1, x2 = list(x1), list(x2)
arr = [0] * 101
res ="No"

for x, y in segments:
    for i in range(x, y+1):
        arr[i] +=1

for i in arr:
    if i == n:
        res = "Yes"
        break

print(res)


