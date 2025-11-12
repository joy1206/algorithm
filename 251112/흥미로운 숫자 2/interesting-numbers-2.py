X, Y = map(int, input().split())

answer = 0

def intersting(i) :
    s = str(i)
    length = len(str(i))
    if len(set(s)) != 2:
        return False
    num1, num2 = list(set(s))
    count1 = s.count(num1)
    count2 = s.count(num2)

    if count1 == 1 and count2 == length -1:
        return True
    elif count2 == 1 and count1 == length -1:
        return True
    return False 


for i in range(X, Y+1):
    if intersting(i):
        answer +=1
print(answer)

