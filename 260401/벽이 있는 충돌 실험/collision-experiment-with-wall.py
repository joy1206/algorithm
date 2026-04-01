import sys

# 테스트 케이스 수
t_str = sys.stdin.readline().strip()
if t_str:
    t = int(t_str)
    for _ in range(t):
        n, m = map(int, sys.stdin.readline().split())
        
        # 주인님의 방식대로 구슬 정보 저장
        marbles = []
        for _ in range(m):
            # 1-based index를 0-based로 바꿔서 저장하는 게 계산하기 편해요!
            r, c, d = sys.stdin.readline().split()
            marbles.append([int(r)-1, int(c)-1, d])

        # 주인님이 정의하신 상 하 좌 우 방향 벡터
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        # 2*n + 1초 동안 시뮬레이션
        for _ in range(2 * n + 1):
            # [중요!] temp_grid는 구슬 하나당 만드는 게 아니라, 1초마다 딱 한 번만 만듭니다!
            temp_grid = [[0] * n for _ in range(n)]
            next_marbles = []

            for i in range(len(marbles)):
                x, y, d = marbles[i]
                
                # 주인님의 if/elif 로직 그대로 사용!
                if d == 'U':
                    nx, ny = x + dx[0], y + dy[0]
                elif d == 'D':
                    nx, ny = x + dx[1], y + dy[1]
                elif d == 'L':
                    nx, ny = x + dx[2], y + dy[2]
                else: # 'R'
                    nx, ny = x + dx[3], y + dy[3]

                # 1. 격자 안으로 이동 가능한 경우
                if 0 <= nx < n and 0 <= ny < n:
                    x, y = nx, ny
                # 2. 벽에 부딪히면 방향만 반전 (주인님의 else 로직)
                else:
                    if d == 'U': d = 'D'
                    elif d == 'D': d = 'U'
                    elif d == 'L': d = 'R'
                    else: d = 'L'
                
                # 이동한(혹은 방향 바꾼) 결과를 임시 리스트에 저장
                next_marbles.append([x, y, d])
                # 공용 격자에 구슬 개수 표시
                temp_grid[x][y] += 1

            # 충돌 체크: temp_grid 값이 1인 구슬만 살아남기
            survivors = []
            for x, y, d in next_marbles:
                if temp_grid[x][y] == 1:
                    survivors.append([x, y, d])
            
            # 살아남은 구슬들로 업데이트
            marbles = survivors
            
            # 구슬이 다 사라지면 조기 종료
            if not marbles:
                break

        print(len(marbles))