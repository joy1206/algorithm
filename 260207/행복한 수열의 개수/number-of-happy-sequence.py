n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
if m == 1:
    ans = n * 2
else:
    ans = 0
    for i in range(n):
        max_cnt, cnt = 1, 1
        for j in range(n-1):
            if arr[i][j] == arr[i][j+1] : cnt +=1
            else: cnt = 1
            
            if cnt > max_cnt:
                max_cnt = cnt
        
        if max_cnt >= m:
            ans += 1


    for j in range(n):
        max_cnt, cnt = 1, 1
        for i in range(n-1):
            if arr[i][j] == arr[i+1][j] : cnt +=1
            else:
                cnt = 1 
                
            if cnt > max_cnt:
                max_cnt = cnt
        
        if max_cnt >= m:
            ans += 1

print(ans)