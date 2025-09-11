arr = list(input())

answer = 0

for i in range(len(arr)-2):
    if arr[i] == '(' and arr[i+1] == '(':
        # (( 발견
        for j in range(i+2,len(arr)-1):
            if arr[j] == ")" and arr[j+1] == ')':
                answer +=1

print(answer)      
