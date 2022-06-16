def solution(n, arr1, arr2):
    answer = []
    for num1, num2 in zip(arr1, arr2) :
        short_str = ''
        drop_the_bit = str(bin(num1 | num2)[2:])
        secret_map = drop_the_bit.replace('1',"#").replace('0'," ")
        if len(secret_map) < n :
            short_str += " " * (n-len(secret_map)) + secret_map
            answer.append(short_str)
        else :
            answer.append(secret_map)
    return answer
