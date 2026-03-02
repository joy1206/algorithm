arr = list(input())
n = len(arr)
min_len = 21e8
temp = arr[:]
for _ in range(n):
    rle = 0
    cnt = 1
    for j in range(n):
        if j < n-1 and temp[j] == temp[j+1]:
            cnt +=1
        else:
            rle += 1 + len(str(cnt))

    if rle < min_len:
        min_len = rle
    
    temp = [temp[-1]] + temp[:-1]

print(min_len)