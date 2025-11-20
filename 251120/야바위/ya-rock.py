n = int(input())
moves = [list(map(int, input().split())) for _ in range(n)]
scores = [0,0,0]
for initial_pos in range(1, 4):
    stone = initial_pos
    current_stone_pos = initial_pos-1
    
    for a, b, c in moves:
        if stone == a:
            stone = b
        elif stone == b:
            stone = a
        
        if stone == c:
            scores[current_stone_pos] +=1

print(max(scores))


