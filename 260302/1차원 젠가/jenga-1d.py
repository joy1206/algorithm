n = int(input())
blocks = [int(input()) for _ in range(n)]

end_of_array = n

def cut_array(start, end):
    global blocks, end_of_array
    temp = []

    for i in range(end_of_array):
        if i < start or i > end:
            temp.append(blocks[i])

    end_of_array = len(temp)
    for i in range(end_of_array):
        blocks[i] = temp[i]

for _ in range(2):
    s, e = tuple(map(int, input().split()))
    cut_array(s-1, e-1)

print(end_of_array) 
for i in range(end_of_array):
    print(blocks[i])