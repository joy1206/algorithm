a = list(map(int, input().split()))
a.sort()
cnt = 0

while True:
    if a[0] == a[1] -1 and a[1] == a[2]-1 :
        break
    else:
        a[-1] = a[1] -1
        a.sort()
        cnt += 1       

print(cnt) 