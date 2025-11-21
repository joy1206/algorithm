n = int(input())
ranges = [tuple(map(int, input().split())) for _ in range(n)]
flag = True

for x in range(1, 10001):
    current_num = x
    is_valid_x = True 

    for a, b in ranges:
        next_num = current_num * 2

        if a <= next_num <= b:
            current_num = next_num 
        else:
            is_valid_x = False
            break 
        
    if is_valid_x:
        print(x)
        break
        