N = int(input())
a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())

count = 0

def solution(x, y):
    return abs(x-y)<=2 or N- abs(x-y)<=2

for i in range(1, N+1):
    for j in range(1, N+1):
        for k in range(1, N+1):
            if solution(i, a1) and solution(j, b1) and solution(k, c1):
                count +=1
            elif solution(i, a2) and solution(j, b2) and solution(k, c2):
                count +=1
print(count)
            


    