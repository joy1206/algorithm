n = int(input())
arr = [tuple(map(str, input().split())) for _ in range(n)]
scores = {'A':0, 'B':0}
cnt = 0
stage = 'AB'

for person, score in arr:
    current_stage = ''
    if person == 'A':
        scores['A'] += int(score)
    else:
        scores['B'] += int(score)
   
    if scores['A'] > scores['B']:
        current_stage = 'A'
    elif scores['B'] > scores['A']:
        current_stage = 'B'
    else:
        current_stage = 'AB'
    

    if stage != current_stage:
        cnt += 1
        stage = current_stage
print(cnt)


