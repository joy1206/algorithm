n = int(input())
h = [int(input()) for _ in range(n)]

ans = 0

for num in range(1, 1000):
    current_lumps = 0
    is_in_lump = False
    for height in h:
        if height > num:
            if not is_in_lump:
                current_lumps +=1
                is_in_lump = True
        else:
            is_in_lump = False
    ans = max(ans, current_lumps)
print(ans)




