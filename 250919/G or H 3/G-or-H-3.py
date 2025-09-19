n, k = map(int, input().split())

locations = {}

for _ in range(n):
    pos, char = input().split()
    locations[int(pos)] = char

end = 10001
score_arr = [0] * 10001

for pos, char in locations.items():
    if char == 'G':
        score_arr[pos] = 1
    elif char == 'H':
        score_arr[pos] = 2

max_score = 0

for i in range(1, end-k):
    temp = 0
    for j in range(k+1):
        if i+j < end:
            temp += score_arr[i+j]
    if max_score < temp:
        max_score = temp
print(max_score)

