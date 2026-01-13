import copy
n = int(input())
a = [0] + list(map(int, input().split()))

arr = copy.deepcopy(a)
arr.sort()

ans = -1
second_min = 0
cnt = 0

for i in range(1, n):
    if arr[i] != arr[i+1]:
        second_min = arr[i+1]
        break

for i in range(1, n+1):
    if a[i] == second_min:
        cnt +=1
        ans = i

if cnt == 1:
    print(ans)
else:
    print(-1)


