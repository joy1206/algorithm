nums = list(map(int, input().split()))
nums.sort()

A = nums[0]
B = nums[1]
C = 0;
if A+B == nums[2]:
    C = nums[3]
else : C = nums[2]

D = nums[-1] - (A + B + C)

print(A, B, C, D)
