def solution(s):
    answer = True
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        else:
            if len(stack) == 0:
                return False
            else:
                if stack:
                    stack.pop()
    if stack:
        answer = False
    return answer