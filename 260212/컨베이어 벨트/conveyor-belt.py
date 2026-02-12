n, t = map(int, input().split())
arr = list(map(int, input().split())) + list(map(int, input().split()))

for _ in range(t):
    arr = [arr[-1]] + arr[:-1]

print(*arr[:n])
print(*arr[n:])


