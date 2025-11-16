n = int(input())
a = list(map(int, input().split()))
k = max(a)
cnt = {}

for i in range(n):
    for j in range(i+1, n):
        s = a[i] + a[j]
        if s % 2 == 0 :
            k = s // 2 
            if k not in cnt : cnt[k] = 1
            else : cnt[k] +=1

ans = max(cnt.values())
print(ans)
            

