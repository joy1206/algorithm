n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]
cnt = 0

for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if i == j or j == k or i == k : continue

            succeeded = True
            for a, cnt1, cnt2 in arr:
                x = a // 100
                y = a // 10 % 10
                z = a % 10

                count1 = 0
                count2 = 0

                if x == i : count1 +=1
                if y == j : count1 +=1
                if z == k : count1 +=1

                if x == j or x == k : count2 +=1
                if y == i or y == k : count2 +=1
                if z == i or z == j : count2 +=1

                if cnt1 != count1 or cnt2 != count2:
                    succeeded = False
                    break
            if succeeded:
                cnt +=1
print(cnt)   