pos = list(map(int, input().split()))
pos.sort()
if pos[0]+1 == pos[1] and pos[1]+1 == pos[2]:
    print(0)

elif pos[0]+2 == pos[1] or pos[1] + 2 == pos[2]:
    print(1)
else:
    print(2)