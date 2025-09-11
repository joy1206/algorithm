n = int(input())
S = list(input())

answer = 0
#가능한 조합의 개수

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1,n):
            if S[i] == 'C' and S[j] == 'O' and S[k] == 'W':
                answer += 1
print(answer)
