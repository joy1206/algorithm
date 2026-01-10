N = int(input())
moves = [tuple(map(int, input().split())) for _ in range(N)]

cases = [
    ('S', 'R', 'P'), ('S', 'P', 'R'),
    ('R', 'S', 'P'), ('R', 'P', 'S'),
    ('P', 'S', 'R'), ('P', 'R', 'S')
]

ans = 0
for case in cases:
    current_wins = 0
    for a,b in moves:
        move_a = case[a -1]
        move_b = case[b-1]

        if (move_a == 'S' and move_b == 'P') or (move_a == 'R' and move_b == 'S') or (move_a == 'P' and move_b == 'R') :
            current_wins += 1

    ans = max(ans, current_wins) 

print(ans)
