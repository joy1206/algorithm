def solution(n, words):
    # 전에꺼도 기억해야함 앞사람이 말한 단어의 마지막 문자로 시작하는 단어를 말해야 
    # 이전에 등장했던 단어는 사용할 수 없습니다.
    # 가장 먼저 탈락하는 사람의 번호와 그 사람이 자신의 몇 번째 차례에 탈락하는지
    num = 0
    turn = 0
    said = []
    for i in range(len(words)):
        if words[i] in said or i > 0 and words[i][0] != said[i-1][-1]:
            num = (i%n)+1
            turn = (i//n)+1
            return [num, turn]
        said.append(words[i])

    return [0, 0]