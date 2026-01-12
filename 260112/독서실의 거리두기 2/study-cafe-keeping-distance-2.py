N = int(input())
seats_str= input()
seats = []
for char in seats_str:
    seats.append(char)

ans = 0

for i in range(N):
    if seats[i] == '0':
        seats[i] = '1'
        
        pos = []
        for j in range(N):
            if seats[j] == '1':
                pos.append(j)

        min_dist = 1001
        for k in range(len(pos)-1):
            dist = pos[k+1] - pos[k]
            if dist < min_dist:
                min_dist = dist

        if min_dist > ans:
            ans = min_dist

        seats[i] = '0'

print(ans)

