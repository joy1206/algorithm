n = int(input())
arr = [list(map(int, input().split()))for _ in range(n)]

def solution(arr):
    for i in range(n):
        cnt = 0
        for j in range(1,n):
            if i == j: continue
            if arr[j-1][1] < arr[j][0] or arr[j][1] < arr[j-1][0]:
                continue
            else:
                cnt += 1
        if cnt == n - 2 :
            return True
        else:
            return False
if solution(arr):
    print('No')
else:
    print('Yes')
