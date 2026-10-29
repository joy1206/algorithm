def solution(participant, completion):
    completion.sort()
    participant.sort()
    answer = []
    
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    
    return participant[-1]
        