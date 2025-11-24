n, k = map(int, input().split())
arr = list(map(int, input().split()))

MAX_NUM = 100

def is_possible(limit):
    last_idx = 0
    for i in range(1, n):
        if arr[i] <= limit:
            if i - last_idx > k:
                return False
            last_idx = i
    return True

for limit in range(max(arr[0], arr[-1]), MAX_NUM +1):
    if is_possible(limit):
        print(limit)
        break
    