n = int(input())
arr = list(input().split())
correct = []
for i in range(n):
    correct.append(ord(arr[i]))
cnt = 0
for i in range(n):
    for j in range(i+1, n):
        if correct[i] > correct[j]:
            cnt +=1
            correct[i], correct[j] = correct[j], correct[i]
print(cnt)
