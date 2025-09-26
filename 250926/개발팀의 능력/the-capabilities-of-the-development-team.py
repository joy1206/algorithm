n = 5
arr = list(map(int, input().split()))
min_diff = 21e8

for i in range(n):
    for j in range(i+1, n):
        for k in range(n):
            for l in range(k+1, n):
                if k == i or k == j or l == i or l == j: continue
                sum1 = arr[i] + arr[j]
                sum2 = arr[k] + arr[l]
                sum3 = sum(arr) - sum1 - sum2  
                # 팀 능력치가 모두 달라야함
                if sum1 == sum2 or sum1 == sum3 or sum2 == sum3 : continue
                ret = abs(sum1 - sum2)
                ret = max(ret, abs(sum2 - sum3))
                ret = max(ret, abs(sum3 - sum1))
                min_diff = min(min_diff, ret)

print(min_diff if min_diff != 21e8 else -1)

