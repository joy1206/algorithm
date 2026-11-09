def solution(number, k):
    answer = ''
    stack = []
    # 4가 들어옴 1이 들어옴 내가 들어왔다 근데 내 앞이 나보다 작으면 걔를 삭제한다.
    for num in number:
        while stack and stack[-1] < num and k>0:
            stack.pop()
            k -= 1
        stack.append(num)
        
    if k>0:
        stack = stack[:-k]
      
    return ''.join(stack)