a = list(input())

answer = 0

for i in range(1, len(a)):
    temp = a[:]
    if temp[i] == '1':
        temp[i] = '0'
    else: temp[i] = '1'

    decimal_value = int("".join(temp), 2)

    if answer < decimal_value:
        answer = decimal_value

print(answer)
        


