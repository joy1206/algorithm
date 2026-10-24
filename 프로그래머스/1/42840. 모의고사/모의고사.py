def solution(answers):
    answer = [0, 0, 0]
    first = [1,2,3,4,5]
    second = [2,1,2,3,2,4,2,5]
    third = [3,3,1,1,2,2,4,4,5,5]
    
    for i in range(len(answers)):
        if answers[i] == first[i % len(first)] :
            answer[0] +=1
        if answers[i] == second[i % len(second)] :
            answer[1] +=1
        if answers[i] == third[i % len(third)] :
            answer[2] +=1
    max_score = max(answer)
    result = []
    for i in range(3):
        if max_score == answer[i]:
            result.append(i+1)
    return result