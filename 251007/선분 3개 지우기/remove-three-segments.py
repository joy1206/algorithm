n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
answer = 0

def solution(lines):
    for i in range(len(lines)):
        for j in range(i+1, len(lines)):
            start_i, end_i = lines[i]
            start_j, end_j = lines[j]
            # 겹치는 경우
            if (start_i <= end_j) and (start_j <= end_i):
                return True
    return False


# i, j, k 3선분을 뺀 나머지 선분끼리 모두 겹치지 않는지 확인
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            result = []
            for l in range(n):
                if l !=i and l!=j and l!=k:
                    result.append(arr[l])
            if not solution(result): answer +=1
print(answer)
                    