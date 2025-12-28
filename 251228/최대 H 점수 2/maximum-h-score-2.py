n, l = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
for i in range(1, n+1):
    cnt = 0
    cntl = 0
    for j in range(n):
        if a[j] >= i:
            cnt +=1
        elif a[j] == i-1:
            if cntl < l:
                cntl += 1
                cnt += 1
    if cnt >= i:
        ans = i
print(ans)