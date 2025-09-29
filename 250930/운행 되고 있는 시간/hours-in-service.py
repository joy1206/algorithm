n = int(input())
times = [tuple(map(int, input().split())) for _ in range(n)]
a = [t[0] for t in times]
b = [t[1] for t in times]

answer = -21e8

for i in range(n):
    # i 해고할 직원
    time_arr = [0] * 1001
    for j in range( n):
        if i == j : continue
        # 나머지 직원들의 시간 배열에 1을 표시
        start_time = times[j][0]
        end_time = times[j][1]

        for k in range(start_time, end_time):
            time_arr[k] = 1
    temp = sum(time_arr)
    answer = max(answer, temp)
print(answer)
