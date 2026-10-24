def solution(nums):
    count_type = len(set(nums))
    can_have = len(nums)//2
    return min(count_type, can_have)


