import sys

n = int(input())
lines = []
for _ in range(n):
    lines.append(list(map(int, input().split())))

for i in range(n):

    for x in range(1, 101):
        all_overlap = True

        for j in range(n):
            if i == j: 
                continue
            
            x1, x2 = lines[j]

            if not (x1 <= x <= x2):
                all_overlap = False
                break
        
        if all_overlap:
            print("Yes")
            sys.exit() 

print("No")