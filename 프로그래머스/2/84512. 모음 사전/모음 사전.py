def solution(word):
    words = [] # 만들 수 있는 단어 리스트

    def dfs(current):
        if len(current) > 5:
            return
        
        if current:
            words.append(current)
        
        for char in "AEIOU":
            dfs(current + char)
        
    dfs("")
    
    return words.index(word) + 1