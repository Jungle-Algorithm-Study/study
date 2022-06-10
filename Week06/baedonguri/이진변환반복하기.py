# s = "110010101001"	
s = "01110"
def solution(s):
    answer = [0,0]
    while True:
        answer[1] += s.count('0')
        tmp = s.replace('0','')
        s = bin(len(tmp))[2:]
        answer[0] += 1
        if s  == "1":
            break
    return answer

print(solution(s))
