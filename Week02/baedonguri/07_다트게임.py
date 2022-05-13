# [프로그래머스] 다트 게임 (python)
# https://programmers.co.kr/learn/courses/30/lessons/17682

dartResult	= '1D2S3T*'
def solution(dartResult):
    string = ''
    bonus = {'S':1, 'D':2, 'T':3}
    scores = []
    cnt = 0         
    for val in dartResult:
        if val.isdigit():
            string += val
        elif val in ['S', 'D', 'T']:
            cnt += 1
            scores.append(int(string)**bonus[val])
            string = ''
        else:
            if val == '*':
                n_len = len(scores)
                scores[n_len-1] *= 2
                if n_len > 1:
                    scores[n_len-2] *= 2

            elif val == '#':
                scores[cnt-1] *= -1
                
    return sum(scores)
    
print(solution(dartResult))