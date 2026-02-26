n, t = map(int, input().split())

l = list(map(int, input().split()))
r = list(map(int, input().split()))
d = list(map(int, input().split()))

arr = l + r + d

total_len = n * 3

t %= total_len

for _ in range(t):
    last = arr.pop()
    arr.insert(0, last)

print(*arr[:n])
print(*arr[n:2*n])
print(*arr[2*n:])


    


