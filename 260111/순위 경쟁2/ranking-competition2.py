n = int(input())
arr = [tuple(map(str, input().split())) for _ in range(n)]
scores = {'A':0, 'B':0}
cnt = 0
stage = ''

for person, score in arr:
    current_stage = ''
    if person == 'A':
        scores['A'] += int(score)
    else:
        scores['B'] += int(score)
    if scores['A'] > scores['B']:
        current_stage = 'A'
    else:
        current_stage = 'B'
    if stage != current_stage:
        cnt +=1
    stage = current_stage
print(cnt)


