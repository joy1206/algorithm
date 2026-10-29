def solution(prices):
    n = len(prices)
    answer = [0] * n
    stack = []
    
    for i in range(n):
        while stack and prices[stack[-1]] > prices[i]:
            prev = stack.pop()
            answer[prev] = i - prev
        stack.append(i)
        
    for s in stack:
        answer[s] = n - s - 1
    
    return answer