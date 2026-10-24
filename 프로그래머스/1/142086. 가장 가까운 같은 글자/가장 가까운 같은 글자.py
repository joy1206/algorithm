def solution(s):
    answer = []
    last = {}
    # 마지막 위치를 알아야한다 -> 마지막 위치를 저장한다
    for i in range(len(s)):
        if s[i] not in last:
            last[s[i]] = i
            answer.append(-1)
        else:
            last_idx = last[s[i]]
            answer.append(i - last_idx)
            last[s[i]] = i
    return answer