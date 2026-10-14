def solution(s, skip, index):
    answer = ''
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    #한칸씩 이동
    # skip에 있으면 continue
    for char in s:
        current = char
        count = 0
        while count < index:
            pos = alphabet.index(current)
            pos = (pos + 1) % 26
            current = alphabet[pos]
            if current in skip : continue
            count += 1
        answer += current     
    return answer