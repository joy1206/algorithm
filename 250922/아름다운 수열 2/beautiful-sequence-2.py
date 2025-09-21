N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

count = 0

# 정렬
B.sort()

for i in range(N-M+1):
    st = A[i:i+M]
    st.sort()

    if st == B:
        count += 1

print(count)
    

    

        

