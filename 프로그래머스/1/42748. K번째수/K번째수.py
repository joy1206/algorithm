def solution(array, commands):
    answer = []
    for i in commands:
        new_list = array[i[0]-1:i[1]]
        new_list.sort()
        num = new_list[i[2]-1]
        answer.append(num)
    return answer