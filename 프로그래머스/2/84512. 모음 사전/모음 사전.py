def solution(word):
    words = []
    def dfs(current):
        if len(current) > 5:
            return 
        if current:
            words.append(current)
        
        for char in "AEIOU":
            dfs(current + char)
            
    dfs("")
   
    return words.index(word) + 1