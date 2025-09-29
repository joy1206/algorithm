n = int(input())
times = [tuple(map(int, input().split())) for _ in range(n)]
a = [t[0] for t in times]
b = [t[1] for t in times]

answer = -21e8

for i in range(n):
    # i 해고할 직원
    for j in range(i+1, n):
        for k in range(j+1, n):
            temp = (times[j][1] - times[j][0]) + (times[k][1] - times[k][0])
            answer = max(answer, temp)

print(answer)
