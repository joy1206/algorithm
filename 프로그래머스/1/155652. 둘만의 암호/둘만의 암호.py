def solution(s, skip, index):
    answer = ''
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    # 한칸씩 이동
    # skip에 있으면 카운트하지 않기
    # index번 유요한 문자로 이동
    # z면 a로 돌아감
    for char in s:
        current = char
        count = 0
        while count < index:
            pos = alphabet.index(current)
            pos = (pos+1) % 26
            current = alphabet[pos]
            if current in skip:
                continue
            count += 1
        answer += current       
    return answer