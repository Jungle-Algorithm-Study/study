import re

def solution(new_id):
    answer = ''

    # Pass 1 : 소문자 처리
    new_id = new_id.lower()
    
    # Pass 2 : 비허용 문자 제거
    answer = re.sub('[^0-9a-z-_.]', "", new_id)

    # Pass 3 : '..' > '.' 처리
    answer = re.sub('[..]+', '.', answer)

    # Pass 4 : 맨 앞 '.' 제거
    answer = re.sub('^[.]', "", answer)    
    
    # Pass 5 : 문자열 길이가 0일 때 처리
    answer = 'a' if not answer else answer    
    
    # Pass 6 : 16자 컷, 맨 뒤 '.' 제거
    answer = answer[:15] if len(answer) >= 16 else answer    
    answer = re.sub('[.]$', "", answer)
    
    # Pass 7 : 3글자 미만 처리
    while len(answer) < 3 : 
        answer += answer[-1]
    
    return answer


# Test case
string = "...!@BaT#*..y.abcdefghi.jklm..." #bat.y.abcdefghi
print(solution(string))
