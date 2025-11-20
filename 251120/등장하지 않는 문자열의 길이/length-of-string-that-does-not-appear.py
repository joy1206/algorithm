N = int(input())
S = input()

for L in range(1, N+1):
    substrings = []

    # 1. 모든 길이 L의 부분 문자열 추출
    for i in range(N-L+1):
        substrings.append(S[i : i+L])
        
    is_unique_length = True

    # substrings = [A, B, C, D, A, B, C]
    for i in range(len(substrings)):
        for j in range(i+1, len(substrings)):
            if substrings[i] == substrings[j]:
                is_unique_length = False
                break
        if not is_unique_length: break

    if is_unique_length :
        ans = L
        break
print(ans)

