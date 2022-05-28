to_bin = lambda n: bin(n)[2:]
MAX = 1000000
def solution(n):
    answer = n
    
    while answer < MAX:
        answer += 1
        if to_bin(n).count("1") == to_bin(answer).count("1"):
            # 그냥 bin만 해도 되는 줄 몰랐습니다 ㅎ
            return answer
        
    return answer
