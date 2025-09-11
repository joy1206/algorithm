n = int(input())
a = [int(input()) for _ in range(n)]

answer = 21e8

# i 는 시작할 방의 번호
    
for i in range(n):
    dis = 0
    # [i번에서 j번까지 거리] * [j번방으로 가야하는 사람 명수]
    for j in range(n):
        if i == j : continue
        # 반시계 방향 처리
        dis += ((j-i+n) % n) * a[j]
    answer = min(answer, dis)

print(answer)
