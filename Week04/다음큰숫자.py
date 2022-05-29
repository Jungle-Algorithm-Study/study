def count(a):
        count = 0
        for i in a :
            if i == "1" :
                count += 1
        return count
    
def solution(n):
    answer, next_num, next_num_count = 0, n, 0
    first_num = bin(n)
    first_num_count = count(first_num)
    while (first_num_count  != next_num_count) :
        next_num_count= 0
        next_num += 1
        c = bin(next_num)
        next_num_count = count(c)                
    return next_num
