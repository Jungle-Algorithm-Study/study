def solution(s):
    n = len(s)
    answer = n
    
    for cut_len in range(1, n//2 + 1):
        current_part = s[:cut_len] # 최초 탐색 부분
        result = ""
        count = 1
        
        for i in range(cut_len, n, cut_len):
            # 현재 탐색하는 부분과 일치하는 한 count를 1씩 올려준다
            if current_part == s[i:i+cut_len]:
                count += 1
                
            else: # 다른 부분이 나온 경우, 탐색할 부분을 새로운 부분으로 갱신하고 
                result += str(count if count > 1 else "") + current_part
                count = 1
                current_part = s[i:i+cut_len]
                
        # 문자열이 끝날 때까지 for의 if를 통과한 경우, result에 추가가 안 되기 때문에 따로 처리
        result += str(count if count > 1 else "") + current_part
        answer = min(answer, len(result))

    return answer
