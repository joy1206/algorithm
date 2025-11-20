arr = []
members = []
ans = 0

for _ in range(3):
    row = list(map(int, input()))
    for i in row:
        if i not in members:
            members.append(i)
    arr.append(row)

def solution(a, b):
    global ans
    # 가로탐색
    for row in arr:
        if set(row) == {a, b}:
            ans += 1
            return ans
    # 세로탐색
    transposed = zip(*arr)
    for row in transposed:
        if set(row) == {a, b}:
            ans += 1
            return ans

    # 대각선 탐색
    if (set((arr[0][0], arr[1][1], arr[2][2])) == {a,b}) or (set((arr[0][2], arr[1][1], arr[2][0])) == {a, b}):
        ans += 1
        return ans
    
# 2명이 한 팀
length = len(members)
for i in range(length):
    for j in range(i+1, length):
        solution(members[i], members[j])
print(ans)


