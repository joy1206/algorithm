n = int(input())
stage = ['A', 'B', 'C']
scores = {'A': 0, 'B': 0, 'C': 0}
cnt = 0

arr = [tuple(input().split()) for _ in range(n)]

 
for person, score in arr:
    scores[person] += int(score)
    max_score = max(scores.values())
    top_players = []
        
    for p in ['A', 'B', 'C']:
        if scores[p] == max_score:
            top_players.append(p)

    if stage != top_players:
        cnt +=1
        stage= top_players

print(cnt)