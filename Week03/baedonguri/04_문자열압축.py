# [프로그래머스] 문자열압축 (python)
# https://programmers.co.kr/learn/courses/30/lessons/60057

def solution(string):
    answer = len(string)
    result = []
    if answer == 1: return 1

    for i in range(1, len(string)+1):
        b = ''
        cnt = 1
        words = string[:i]

        for j in range(i, len(string)+i, i):
            if words == string[j:j+i]:
                cnt += 1
            else:
                if cnt != 1:
                    b += (str(cnt)+words)
                else:
                    b += words
                cnt = 1
                words = string[j:j+i]
        answer = min(answer, len(b))

    return answer

print(solution("aabbaccc"))
