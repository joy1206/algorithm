def solution(number, limit, power):
    answer = 0

    def count_num(num):
        count = 0
        i = 1
        while i * i <= num:
            if num % i == 0:
                if i * i == num:
                    count += 1
                else:
                    count += 2
            i += 1
        return count   
    
    for i in range(1, number+1):
        count = count_num(i)
        if count > limit:
            answer += power
        else:
            answer += count

    return answer